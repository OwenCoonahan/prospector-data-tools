# Grid Stress Monitor

Real-time visualization of grid congestion, constraints, and stress points across US Independent System Operators (ISOs).

![Grid Stress Monitor Screenshot](screenshots/grid-stress-monitor.png)

## Overview

The Grid Stress Monitor provides a unified view of electrical grid stress indicators across all major US ISOs:

- **ERCOT** (Texas)
- **PJM** (Mid-Atlantic + Midwest)
- **CAISO** (California)
- **MISO** (Central US)
- **SPP** (Great Plains)
- **NYISO** (New York)
- **ISO-NE** (New England)

## Features

### Map Visualization
- **LMP Heat Points**: Sized and colored by price/stress level
- **Constraint Lines**: Animated lines showing binding transmission constraints
- **Interactive Popups**: Click any point for detailed LMP breakdown (Energy, Congestion, Loss)

### Stress Indicators
| Level | Color | Criteria |
|-------|-------|----------|
| Critical | Red | LMP > $80/MWh |
| High | Orange | LMP $50-80/MWh |
| Elevated | Blue | LMP $30-50/MWh |
| Normal | Gray | LMP < $30/MWh |
| Curtailment | Green | Negative LMP |

### Sidebar Panels
- **Active Alerts**: Grid warnings, conservation appeals, TLR events
- **Top Constraints**: Ranked by shadow price ($/MWh)
- **Peak Statistics**: Highest/lowest LMP, max spread
- **24h LMP Chart**: Historical trend for selected zone

## Data Sources

See [RESEARCH.md](RESEARCH.md) for full data source documentation.

Key sources:
- ISO real-time LMP feeds
- ERCOT NP6-788-CD (Real-Time LMPs)
- PJM Data Miner 2
- CAISO OASIS
- gridstatus.io (aggregated data)

## Usage

1. Open `index.html` in a browser
2. Use ISO filter buttons to focus on specific regions
3. Click markers for detailed price breakdowns
4. Hover over constraint lines for flow information

## Files

```
grid-stress-monitor/
├── index.html          # Main visualization
├── README.md           # This file
├── RESEARCH.md         # Data source research
├── data/
│   ├── lmp-current.json    # Current LMP by zone
│   ├── lmp-history.json    # 24h historical data
│   ├── constraints.json    # Active constraints
│   ├── alerts.json         # Grid alerts
│   └── iso-zones.json      # Zone boundaries
└── screenshots/
    └── grid-stress-monitor.png
```

## Development

### Adding Live Data

Replace the embedded sample data with API calls:

```javascript
// Example: Fetch from gridstatus API
async function fetchLMPData() {
    const response = await fetch('https://api.gridstatus.io/v1/lmp?iso=ERCOT');
    return response.json();
}
```

### Mapbox Token

The visualization uses a Mapbox public token. For production, replace with your own:

```javascript
mapboxgl.accessToken = 'your-token-here';
```

## Interpretation Guide

### What High LMP Means
- **Demand > Supply** in that zone
- **Transmission limits** preventing cheap power from flowing in
- **Generator scarcity** in the local area

### What Negative LMP Means
- **Oversupply** (usually wind/solar)
- **Transmission bottleneck** preventing export
- **Curtailment likely** - generators being paid to reduce output

### Congestion Component
The congestion portion of LMP directly measures transmission constraint costs:
- High congestion = binding transmission limits
- Negative congestion = export constrained (can't get power out)

## Future Enhancements

- [ ] Real-time WebSocket data feed
- [ ] Historical playback mode
- [ ] Constraint detail drill-down
- [ ] Renewable curtailment overlay
- [ ] Price forecast integration
- [ ] Mobile-responsive improvements

---

*Built with Mapbox GL JS • Dark mode design*
