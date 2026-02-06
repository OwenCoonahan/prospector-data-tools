# Developer Scorecard

A search interface for developer track records in US interconnection queues.

## Features

- **Search by developer name** - Fast fuzzy search through 6,271 developers
- **Developer stats** - Total projects, total MW, success rate, average timeline
- **Project breakdown** - Operational, under construction, pending, withdrawn
- **Detail view** - Click any developer to see full project list
- **Filters** - By region, technology type, minimum MW, minimum projects
- **Ranking** - Sort by total MW, project count, success rate, or timeline
- **Export** - Download filtered results as JSON
- **Dark/Light mode** - System-aware theme toggle

## Data Source

Aggregated from queue database at:
```
/Users/castle-owencoonahan/.openclaw/workspace/queue-analysis-project/tools/.data/queue.db
```

## Files

```
developer-scorecard/
├── index.html          # Single-file web interface
├── data/
│   └── developers.json # Aggregated developer statistics
├── generate_data.py    # Script to regenerate data from database
├── screenshots/
│   ├── light-mode.png
│   └── dark-mode.png
└── README.md
```

## Usage

1. Open `index.html` in a browser
2. Search for developers by name
3. Use filters to narrow results
4. Click a developer row to see detailed stats and project list
5. Export filtered data using the Export button

## Regenerating Data

```bash
python3 generate_data.py
```

This queries the queue database and outputs `data/developers.json`.

## Statistics

| Metric | Value |
|--------|-------|
| Total Developers | 6,271 |
| Total Projects | 34,352 |
| Total Capacity | 2.8+ TW |

## Success Rate Calculation

Success rate is calculated as:
```
(Operational + Under Construction) / (Operational + Under Construction + Withdrawn) × 100
```

Projects still in queue (Active, Suspended, IA Pending, etc.) are excluded from this calculation.

## Design

Follows the design system:
- **Fonts**: Inter (sans) + JetBrains Mono (mono)
- **Colors**: Monochrome palette with `#3B82F6` accent
- **Styling**: No shadows, borders only
- **Theme**: Dark/light mode with system detection

---

*Built for Prospector Labs | Feb 2026*
