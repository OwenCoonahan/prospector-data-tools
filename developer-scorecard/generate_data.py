#!/usr/bin/env python3
"""Generate aggregated developer statistics from queue database."""

import sqlite3
import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

DB_PATH = "/Users/castle-owencoonahan/.openclaw/workspace/queue-analysis-project/tools/.data/queue.db"
OUTPUT_PATH = Path(__file__).parent / "data" / "developers.json"

def parse_date(date_str):
    """Parse date string to datetime."""
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return None

def calculate_timeline_months(queue_date, cod_date):
    """Calculate months between queue date and COD."""
    qd = parse_date(queue_date)
    cd = parse_date(cod_date)
    if not qd or not cd:
        return None
    delta = cd - qd
    return round(delta.days / 30.44)  # average days per month

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    # Fetch all projects with developers
    query = """
    SELECT 
        queue_id,
        name,
        COALESCE(developer_canonical, developer) as developer,
        parent_company,
        capacity_mw,
        type_std as type,
        status_std as status,
        region,
        state,
        queue_date_std as queue_date,
        cod_std as cod
    FROM projects 
    WHERE developer IS NOT NULL AND developer != ''
    ORDER BY developer, queue_date_std
    """
    
    rows = conn.execute(query).fetchall()
    conn.close()
    
    # Aggregate by developer
    developers = defaultdict(lambda: {
        'name': '',
        'projects': [],
        'total_projects': 0,
        'total_mw': 0,
        'operational_count': 0,
        'operational_mw': 0,
        'withdrawn_count': 0,
        'withdrawn_mw': 0,
        'construction_count': 0,
        'construction_mw': 0,
        'pending_count': 0,
        'pending_mw': 0,
        'regions': set(),
        'types': set(),
        'timelines': [],
        'earliest_queue': None,
        'latest_queue': None
    })
    
    for row in rows:
        dev_name = row['developer']
        if not dev_name or len(dev_name.strip()) < 2:
            continue
            
        dev = developers[dev_name]
        dev['name'] = dev_name
        
        mw = row['capacity_mw'] or 0
        status = row['status'] or 'Unknown'
        
        # Add project to list
        project = {
            'id': row['queue_id'],
            'name': row['name'],
            'mw': mw,
            'type': row['type'],
            'status': status,
            'region': row['region'],
            'state': row['state'],
            'queue_date': row['queue_date'],
            'cod': row['cod']
        }
        dev['projects'].append(project)
        
        # Update totals
        dev['total_projects'] += 1
        dev['total_mw'] += mw
        
        # Status breakdown
        if status == 'Operational':
            dev['operational_count'] += 1
            dev['operational_mw'] += mw
        elif status == 'Withdrawn':
            dev['withdrawn_count'] += 1
            dev['withdrawn_mw'] += mw
        elif status == 'Under Construction':
            dev['construction_count'] += 1
            dev['construction_mw'] += mw
        else:  # Active, Suspended, IA Pending, Facilities Study, System Study
            dev['pending_count'] += 1
            dev['pending_mw'] += mw
        
        # Track regions and types
        if row['region']:
            dev['regions'].add(row['region'])
        if row['type']:
            dev['types'].add(row['type'])
        
        # Timeline calculation for operational projects
        if status == 'Operational' and row['queue_date'] and row['cod']:
            timeline = calculate_timeline_months(row['queue_date'], row['cod'])
            if timeline and timeline > 0 and timeline < 240:  # sanity check: < 20 years
                dev['timelines'].append(timeline)
        
        # Track date range
        qd = parse_date(row['queue_date'])
        if qd:
            if not dev['earliest_queue'] or qd < parse_date(dev['earliest_queue']):
                dev['earliest_queue'] = row['queue_date']
            if not dev['latest_queue'] or qd > parse_date(dev['latest_queue']):
                dev['latest_queue'] = row['queue_date']
    
    # Calculate final stats and prepare output
    output = []
    for dev_name, dev in developers.items():
        if dev['total_projects'] < 1:
            continue
            
        # Success rate (operational or under construction vs withdrawn)
        completed = dev['operational_count'] + dev['construction_count']
        decided = completed + dev['withdrawn_count']
        success_rate = round(completed / decided * 100, 1) if decided > 0 else None
        
        # Average timeline
        avg_timeline = round(sum(dev['timelines']) / len(dev['timelines']), 1) if dev['timelines'] else None
        
        record = {
            'name': dev['name'],
            'total_projects': dev['total_projects'],
            'total_mw': round(dev['total_mw'], 2),
            'operational': {'count': dev['operational_count'], 'mw': round(dev['operational_mw'], 2)},
            'withdrawn': {'count': dev['withdrawn_count'], 'mw': round(dev['withdrawn_mw'], 2)},
            'construction': {'count': dev['construction_count'], 'mw': round(dev['construction_mw'], 2)},
            'pending': {'count': dev['pending_count'], 'mw': round(dev['pending_mw'], 2)},
            'success_rate': success_rate,
            'avg_timeline_months': avg_timeline,
            'regions': sorted(dev['regions']),
            'types': sorted(dev['types']),
            'earliest_queue': dev['earliest_queue'],
            'latest_queue': dev['latest_queue'],
            'projects': dev['projects']
        }
        output.append(record)
    
    # Sort by total MW descending
    output.sort(key=lambda x: x['total_mw'], reverse=True)
    
    # Save to file
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(output, f)
    
    print(f"Generated {len(output)} developer records")
    print(f"Output: {OUTPUT_PATH}")
    
    # Print top 10
    print("\nTop 10 by Total MW:")
    for i, dev in enumerate(output[:10], 1):
        print(f"  {i}. {dev['name']}: {dev['total_mw']:,.0f} MW ({dev['total_projects']} projects)")

if __name__ == '__main__':
    main()
