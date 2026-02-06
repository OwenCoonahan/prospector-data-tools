# US ISO Queue Comparison Dashboard

Side-by-side comparison of interconnection queue metrics across all major US Independent System Operators (ISOs) and Regional Transmission Organizations (RTOs).

## Live Demo

Open `index.html` in a browser.

## Data Source

Aggregated from the queue analysis database at:
```
/queue-analysis-project/tools/.data/queue.db
```

Data covers 9 regions: PJM, MISO, ERCOT, CAISO, SPP, West (WECC), ISO-NE, NYISO, and Southeast.

## Metrics Compared

| Metric | Description |
|--------|-------------|
| **Queue Size** | Number of projects and total MW in queue |
| **Withdrawal Rate** | % of projects that withdrew from the queue |
| **Completion Rate** | % of projects reaching operational status |
| **Average Timeline** | Years from queue entry to commercial operation |
| **Capacity Mix** | Breakdown by technology (solar, wind, storage, gas, other) |
| **Average Project Size** | Mean MW per project |
| **Queue Growth** | Annual new entries trend (2019-2024) |

## Key Findings

- **Largest queue by projects:** PJM (8,152 projects)
- **Largest queue by capacity:** West (1,133 GW)
- **Highest withdrawal rate:** SPP (89%)
- **Highest completion rate:** ISO-NE (18.5%)
- **Longest average timeline:** NYISO (5.9 years)
- **Largest avg project size:** CAISO (250 MW)

## Files

```
iso-comparison/
├── index.html          # Interactive dashboard
├── data/
│   └── iso-stats.json  # Aggregated metrics
├── screenshots/
│   ├── light.jpg       # Light mode screenshot
│   └── dark.jpg        # Dark mode screenshot
└── README.md
```

## Design

Follows DESIGN_SYSTEM.md:
- Light mode default (report-style)
- Horizontal bars for all comparisons
- Gray context, single accent color for highlights
- Clean typography hierarchy
- Tabular numbers for data alignment

## Tech Stack

- Pure HTML/CSS/JS (no dependencies)
- CSS custom properties for theming
- Responsive grid layout

---

Built by [Prospector Labs](https://prospectorlabs.io) • Feb 2026
