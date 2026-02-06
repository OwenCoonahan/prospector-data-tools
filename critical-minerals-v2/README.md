# Critical Minerals Tracker v2

A comprehensive dashboard tracking rare earth and critical minerals supply chains powering the energy transition.

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Data](https://img.shields.io/badge/data-February%202026-blue)
![Version](https://img.shields.io/badge/version-2.0-purple)

## Overview

This tracker monitors 12 critical minerals essential for EVs, batteries, solar panels, and semiconductors:

| Mineral | Symbol | Primary Use | Data Quality |
|---------|--------|-------------|--------------|
| **Lithium** | Li | EV Batteries | ⭐⭐⭐⭐⭐ Excellent |
| **Cobalt** | Co | EV Batteries | ⭐⭐⭐⭐ Good |
| **Nickel** | Ni | Batteries, Steel | ⭐⭐⭐⭐⭐ Excellent |
| **Copper** | Cu | Electrical, EVs | ⭐⭐⭐⭐⭐ Excellent |
| **Graphite** | C | Battery Anodes | ⭐⭐⭐⭐ Good |
| **Manganese** | Mn | Batteries, Steel | ⭐⭐⭐⭐ Good |
| **Rare Earths** | REE | Magnets, Motors | ⭐⭐⭐ Moderate |
| **Silicon** | Si | Solar, Semis | ⭐⭐⭐⭐ Good |
| **Gallium** | Ga | Semiconductors | ⭐⭐ Limited |
| **Germanium** | Ge | Fiber Optics | ⭐⭐ Limited |
| **Tellurium** | Te | Thin-film Solar | ⭐⭐⭐ Moderate |

## 🆕 New in v2.0

### Company-Level Data
- **70+ company profiles** across all minerals
- Mining and processing companies with tickers, HQ, market share
- Key assets and recent M&A news
- Direct links to company websites

### Trade Flow Visualization
- **Sankey diagrams** showing material flow from mine to end-use
- Export/import relationships by country
- Processing bottleneck identification

### Supply Chain Intelligence
- **6-stage supply chains** for each mineral
- Processing methods and products at each stage
- Geographic concentration at every step
- Critical bottleneck highlighting

## Features

- 📊 **Real-time prices** from Trading Economics, LME, COMEX
- 🌍 **Production data** by country with concentration risk analysis
- 📈 **Reserve estimates** from USGS Mineral Commodity Summaries
- 🔗 **Sankey diagrams** for supply chain flows
- ⚠️ **Risk indicators** for single-country supply dominance
- 🏢 **Company profiles** with key assets and news
- 📈 **Trade flow analysis** export/import relationships

## Key Findings

### Supply Concentration Risks (Critical)
| Mineral | Stage | Dominant Country | Share |
|---------|-------|-----------------|-------|
| Gallium | Production | China | 96% |
| Graphite | Anode Processing | China | 95% |
| REE | Magnet Manufacturing | China | 92% |
| REE | Separation | China | 90% |
| Cobalt | Refining | China | 72% |
| Cobalt | Mining | DR Congo | 68% |
| Lithium | Processing | China | 65% |
| Nickel | Mining | Indonesia | 50% |

### Top Companies by Mineral
| Mineral | #1 Company | #2 Company | #3 Company |
|---------|------------|------------|------------|
| Lithium | Albemarle (USA) | SQM (Chile) | Ganfeng (China) |
| Cobalt | Glencore (Swiss) | CMOC (China) | ERG (Lux) |
| Nickel | Tsingshan (China) | Vale (Brazil) | Nornickel (Russia) |
| Copper | Codelco (Chile) | Freeport (USA) | BHP (Australia) |
| REE | China Northern (China) | MP Materials (USA) | Lynas (Australia) |
| Graphite | BTR (China) | Shanshan (China) | Syrah (Australia) |

### Current Prices (Feb 2026)
- **Lithium Carbonate:** 134,500 CNY/t (+74% YoY)
- **Cobalt:** $56,290/t (+161% YoY)
- **Nickel:** $17,033/t (+8% YoY)
- **Copper:** $5.85/lb (+28% YoY)

## Project Structure

```
critical-minerals-v2/
├── index.html              # Main dashboard
├── data/
│   ├── minerals.json       # Mineral data (prices, production, reserves)
│   ├── companies.json      # 70+ company profiles by mineral
│   ├── trade-flows.json    # Sankey/export-import data
│   ├── supply-chain-steps.json  # Processing stages per mineral
│   └── supply-chains.json  # Legacy supply chain flow data
├── screenshots/            # Dashboard screenshots
├── DATA_SOURCES.md         # Detailed source documentation
└── README.md               # This file
```

## Data Files

### `companies.json`
Company profiles for each mineral including:
- Mining companies (top 10 with market share)
- Processing/refining companies
- Tickers, exchanges, HQ locations
- Key assets and recent news
- Concentration risk metrics

### `trade-flows.json`
Trade flow data for Sankey visualization:
- Nodes: Mining → Processing → Manufacturing → End Use
- Links: Percentage flows between stages
- Export routes: Major bilateral relationships
- Import data: Who depends on whom

### `supply-chain-steps.json`
Detailed processing stages:
- 6 stages from ore to final product
- Products at each stage
- Processing methods
- Geographic locations
- Bottleneck identification

## Data Sources

### Free Public Sources (Used)
- **USGS Mineral Commodity Summaries 2024** — Production, reserves
- **Trading Economics** — Daily prices (CFD-based)
- **LME** — Nickel, cobalt prices
- **Company Filings** — Annual reports, investor presentations
- **UN Comtrade** — Trade flow data
- **IEA Critical Minerals Outlook** — Processing concentrations

### Paid Sources (For Enhanced Data)
- **Benchmark Mineral Intelligence** — Battery materials ($$$)
- **S&P Global / Platts** — All commodities ($$$)
- **Fastmarkets** — Battery metals ($$$)
- **Asian Metal** — Rare earths, minor metals ($$)

See [DATA_SOURCES.md](DATA_SOURCES.md) for complete source documentation.

## Running Locally

```bash
# Navigate to project
cd critical-minerals-v2

# Serve with any HTTP server
python -m http.server 8000
# or
npx serve

# Open browser
open http://localhost:8000
```

## Design

Follows Prospector Labs design system:
- Dark mode default (charcoal #18181B)
- Single accent color (Electric Blue #3B82F6)
- Geist + JetBrains Mono typography
- Horizontal bar charts for rankings
- Sankey charts for supply chain flows
- No gradients, shadows, or decorative elements
- Color-coded risk badges (Critical/High/Moderate)

## Interactive Views

Each mineral has 4 views:
1. **Overview** — Prices, production, reserves
2. **Companies** — Mining and processing players
3. **Supply Chain** — Processing stages and Sankey diagram
4. **Trade Flows** — Export/import relationships

## Future Enhancements

- [ ] Interactive world map with production/reserves
- [ ] Historical price charts
- [ ] Live API integration for real-time prices
- [ ] Export functionality (PNG, PDF, CSV)
- [ ] Chord diagram for trade relationships
- [ ] M&A tracker with deal values
- [ ] ESG risk scoring

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2026-02-06 | Company data, trade flows, supply chain steps, Sankey diagrams |
| 1.0 | 2026-02-05 | Initial release with country-level data |

## Credits

**Data:**
- U.S. Geological Survey (USGS)
- Trading Economics
- Company annual reports
- IEA Critical Minerals Outlook
- Industry reports and estimates

**Visualization:**
- Chart.js for charts and Sankey diagrams
- Custom CSS for design system

---

*Built by Prospector Labs — prospectorlabs.io*
