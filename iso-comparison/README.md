# US ISO Queue Comparison Dashboard

Interactive side-by-side comparison of interconnection queue metrics across all major US Independent System Operators (ISOs) and Regional Transmission Organizations (RTOs).

## Live Demo

Open `index.html` in a browser.

## Features

### 🎯 Interactive Selection
- **Click any ISO** to highlight it across ALL charts and open a detail panel
- **Compare Mode**: Select 2-3 ISOs to compare them directly (dimming the rest)
- **Hover tooltips** show exact values and ranking for each metric

### 📊 Comprehensive Metrics

| Metric | Description |
|--------|-------------|
| **Queue Size** | Number of projects and total MW in queue |
| **Withdrawal Rate** | % of projects that withdrew from the queue |
| **Completion Rate** | % of projects reaching operational status |
| **Avg Queue Time** | Days active projects have been waiting (backlog indicator) |
| **Median Project Size** | Median MW per project (better than average for skewed data) |
| **Storage Ratio** | % of queue capacity that is storage-related |
| **Hybrid Project %** | % of projects combining technologies (solar+storage, etc.) |
| **Unique Developers** | Number of distinct developers in queue |
| **Capacity Mix** | Breakdown by technology (solar, wind, storage, gas, other) |
| **Queue Growth** | Annual new entries trend with YoY % change |

### 📋 ISO Detail Panel
Click any ISO to see:
- Full name and description
- Key statistics summary
- Top 5 developers in that region
- Historical queue growth trend
- Territory coverage (states)

### 📈 Data Table Enhancements
- **Sortable columns**: Click any header to sort
- **Search/filter**: Quick filter by ISO name
- **Best/Worst highlighting**: Green for best values, red for worst in each column

## Data Source

Aggregated from the queue analysis database at:
```
/queue-analysis-project/tools/.data/queue.db
```

Data covers 9 regions: PJM, MISO, ERCOT, CAISO, SPP, West (WECC), ISO-NE, NYISO, and Southeast.

## Key Findings

- **Largest queue by projects:** PJM (8,152 projects)
- **Largest queue by capacity:** West (1,133 GW)
- **Highest withdrawal rate:** SPP (89%)
- **Highest completion rate:** ISO-NE (18.5%)
- **Longest avg queue time:** CAISO (2,575 days / 7+ years)
- **Highest storage ratio:** CAISO (59.5%)
- **Most hybrid projects:** CAISO (25.2%)
- **Most unique developers:** ERCOT (2,305)

## Files

```
iso-comparison/
├── index.html          # Interactive dashboard (single-file, self-contained)
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
- Dark mode toggle available
- Horizontal bars for all comparisons
- Gray context, single accent color for highlights
- Interactive selection highlighting
- Slide-out detail panel
- Clean typography hierarchy (Geist font)
- Tabular numbers for data alignment

## Tech Stack

- Pure HTML/CSS/JS (no dependencies)
- CSS custom properties for theming
- Responsive grid layout
- Works with file:// protocol (no server needed)

---

Built by [Prospector Labs](https://prospectorlabs.io) • Feb 2026
