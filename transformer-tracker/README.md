# Power Transformer Lead Time Tracker

Interactive visualization tracking the power transformer supply chain constraints affecting the US electric grid.

![Screenshot](screenshots/lead-times.png)

## Overview

Power transformers are a critical bottleneck for grid modernization, renewable energy interconnection, and data center expansion. Lead times for large power transformers have extended from 12-18 months pre-2020 to 36-48+ months at peak shortage.

This tracker visualizes:
- **Lead times** by transformer type (distribution, medium power, large power, GSU)
- **Manufacturer market share** and US manufacturing presence
- **Supply chain constraints** (materials, capacity, labor, testing)
- **Demand drivers** (renewables, data centers, grid modernization)

## Data Quality Warning ⚠️

**This data is largely ESTIMATED.** No comprehensive public database of transformer lead times exists. Data was compiled from:

- Utility IRP filings (Duke, AEP, PG&E, Xcel)
- NERC reliability assessments
- Industry publications (T&D World, Power Engineering)
- Company investor presentations
- Trade data (US Census/ITC HS codes)

See [RESEARCH.md](RESEARCH.md) for detailed methodology and data quality assessment.

## Key Findings

### Lead Times (Current Estimates)
| Type | Pre-2020 | Peak (2022-23) | Current |
|------|----------|----------------|---------|
| Distribution (<5 MVA) | 2-3 mo | 12-18 mo | 8-14 mo |
| Medium Power (5-100 MVA) | 6-12 mo | 24-36 mo | 16-28 mo |
| Large Power (100-400 MVA) | 12-18 mo | 36-60 mo | 28-44 mo |
| GSU (200-1000+ MVA) | 18-24 mo | 48-72 mo | 32-50 mo |

### Manufacturing Landscape
- **6** US facilities capable of producing large power transformers
- **Top 5 manufacturers** control ~65% of global market
- **Hitachi Energy** (~20%), **Siemens** (~15%), **TBEA** (~12%), **GE Vernova** (~10%)
- Several capacity expansions announced (Hyundai AL, Hitachi expansions)

### Critical Constraints
1. **Grain-Oriented Electrical Steel (GOES)** - US 70% import dependent
2. **Manufacturing Capacity** - Limited facilities, $100M+ to build new
3. **Skilled Labor** - 30% of workforce retiring in 10 years
4. **Testing Facilities** - Only ~10 in North America

### Demand Drivers
- 2,600 GW in interconnection queues (each project needs transformers)
- Data center load projected to double by 2030
- 25% of grid transformers past design life
- IRA/clean energy driving record deployment

## Project Structure

```
transformer-tracker/
├── index.html          # Interactive visualization
├── README.md           # This file
├── RESEARCH.md         # Detailed research findings
└── data/
    ├── lead_times.json     # Lead time data by transformer type
    ├── manufacturers.json  # Manufacturer profiles and market share
    ├── constraints.json    # Supply chain constraints
    └── demand_drivers.json # Demand driver analysis
```

## Running Locally

Simply open `index.html` in a browser. No build step required.

## Data Gaps & Future Work

Key data that doesn't exist publicly:
- Real-time order backlog by manufacturer
- Manufacturing capacity utilization rates
- Inventory levels at utilities
- Failure/replacement rates

Potential approaches:
- FOIA requests to DOE for survey data
- Systematic scraping of utility IRP filings
- Monitoring manufacturer earnings calls
- Building industry relationships

## Design

Follows [DESIGN_SYSTEM.md](../DESIGN_SYSTEM.md):
- Dark mode interface
- Horizontal bar charts for comparisons
- Single accent color (Electric blue #3B82F6)
- Inter + JetBrains Mono typography
- Minimal, data-forward design

## Sources

- DOE Large Power Transformer Study (2014)
- NERC Long-Term Reliability Assessment (2024)
- Various utility IRP filings
- T&D World, Power Engineering coverage
- Company investor presentations

## License

Data compiled for research purposes. Original sources retain their copyright.

---

*Prospector Labs — February 2026*
