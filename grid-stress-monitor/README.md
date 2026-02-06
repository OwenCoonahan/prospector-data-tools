# Grid Stress Monitor

Real-time visualization of grid congestion, constraints, and stress points across US Independent System Operators (ISOs).

![Grid Stress Monitor Screenshot](screenshots/grid-stress-monitor.png)

---

## 🟢 Live Data Integration (v2.0)

This dashboard now integrates **live real-time data** from ERCOT with automatic fallback to sample data for other ISOs.

### Data Sources

| Source | Data Type | Update Frequency | Status |
|--------|-----------|------------------|--------|
| **ERCOT** | Real-time LMPs (Hub/Zone) | 5 minutes | ✅ Live |
| **ERCOT** | Fuel Mix by Type | 5 minutes | ✅ Live |
| **ERCOT** | Supply/Demand | 5 minutes | ✅ Live |
| **PJM, CAISO, etc.** | Sample Data | — | 📊 Sample |

### New Features (v2.0)

- **Real-time LMP markers** with live ERCOT data
- **Fuel generation mix** bar chart (Wind, Solar, Gas, Nuclear, etc.)
- **System stats**: Load (GW), Reserve Margin, Renewable %
- **Live/Sample badge** shows data source status
- **Manual refresh button** + 5-minute auto-refresh
- **Improved legend** with color scale
- **Enhanced styling** following design system

See [LIVE_DATA_SOURCES.md](LIVE_DATA_SOURCES.md) for complete API documentation.

---

## Overview

The Grid Stress Monitor provides a unified view of electrical grid stress indicators across all major US ISOs:

- **ERCOT** (Texas) — 🟢 Live Data
- **PJM** (Mid-Atlantic + Midwest)
- **CAISO** (California)
- **MISO** (Central US)
- **SPP** (Great Plains)
- **NYISO** (New York)
- **ISO-NE** (New England)

## Features

### Map Visualization
- **LMP Heat Points**: Sized and colored by price/stress level
- **Interactive Popups**: Click any point for detailed LMP breakdown
- **ISO Filtering**: Focus on specific regions

### Stress Indicators
| Level | Color | Criteria |
|-------|-------|----------|
| Critical | Red | LMP > $80/MWh |
| High | Orange | LMP $50-80/MWh |
| Elevated | Blue | LMP $30-50/MWh |
| Normal | Gray | LMP < $30/MWh |
| Curtailment | Green | Negative LMP |

### Left Sidebar
- **System Overview**: Load, Reserve Margin, Renewable %, Binding Constraints
- **Generation Mix**: Real-time fuel breakdown with stacked bar
- **Active Alerts**: Grid warnings and events

### Right Sidebar
- **ISO Filter**: Quick filter by region
- **Peak Statistics**: Highest/lowest LMP, max spread
- **Top Constraints**: Ranked by shadow price
- **24h LMP Chart**: Historical trend

## Live Data API Endpoints

### ERCOT (Working)
```
Hub/Zone LMPs: https://www.ercot.com/content/cdr/html/hb_lz.html
Fuel Mix:      https://www.ercot.com/api/1/services/read/dashboards/fuel-mix.json
Supply/Demand: https://www.ercot.com/api/1/services/read/dashboards/supply-demand.json
```

### EIA (Hourly Demand)
```
https://api.eia.gov/v2/electricity/rto/region-data/data/?api_key=DEMO_KEY&...
```

See [LIVE_DATA_SOURCES.md](LIVE_DATA_SOURCES.md) for complete details.

## Usage

1. Open `index.html` in a browser
2. Dashboard auto-fetches live ERCOT data on load
3. Use ISO filter buttons to focus on specific regions
4. Click markers for detailed price breakdowns
5. Manual refresh available via button in header
6. Data auto-refreshes every 5 minutes

### Data Status Indicators

| Badge | Meaning |
|-------|---------|
| 🟢 LIVE | Successfully fetching real-time data |
| 🟡 SAMPLE | Using sample data (API unavailable) |
| 🔴 OFFLINE | Fetch failed, using fallback |

## Files

```
grid-stress-monitor/
├── index.html              # Main visualization (v2.0)
├── README.md               # This file
├── RESEARCH.md             # Data source research
├── LIVE_DATA_SOURCES.md    # API documentation (NEW)
├── data/
│   ├── lmp-current.json    # Sample LMP data
│   ├── constraints.json    # Active constraints
│   └── iso-zones.json      # Zone boundaries
└── screenshots/
    └── grid-stress-monitor.png
```

## Development

### CORS Notes

All ERCOT endpoints return proper CORS headers. Direct browser fetch works without proxy.

### Mapbox Token

The visualization uses a Mapbox public token. For production, replace with your own:

```javascript
mapboxgl.accessToken = 'your-token-here';
```

### Adding More ISOs

Other ISOs (PJM, CAISO, MISO, NYISO, SPP) require:
- API registration (PJM Data Miner)
- OASIS accounts (CAISO)
- Proxy server (CORS issues)

See LIVE_DATA_SOURCES.md for specifics.

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

- [x] Real-time ERCOT data integration
- [x] Fuel mix visualization
- [x] System stats dashboard
- [ ] EIA hourly demand integration
- [ ] MISO API (new JSON format)
- [ ] PJM Data Miner API key
- [ ] Historical playback with time slider
- [ ] Constraint detail drill-down
- [ ] Mobile-responsive improvements

---

*Built with Mapbox GL JS • Live ERCOT Data • Dark mode design*
