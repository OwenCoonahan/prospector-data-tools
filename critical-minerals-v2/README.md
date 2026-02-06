# Critical Minerals Tracker v2

A comprehensive dashboard tracking rare earth and critical minerals supply chains powering the energy transition.

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Data](https://img.shields.io/badge/data-February%202026-blue)

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

## Features

- 📊 **Real-time prices** from Trading Economics, LME, COMEX
- 🌍 **Production data** by country with concentration risk analysis
- 📈 **Reserve estimates** from USGS Mineral Commodity Summaries
- 🔗 **Supply chain flows** from mine to end use
- ⚠️ **Risk indicators** for single-country supply dominance
- 🏢 **Major companies** in each mineral sector

## Key Findings

### Supply Concentration Risks (Critical)
| Mineral | Stage | Dominant Country | Share |
|---------|-------|-----------------|-------|
| Gallium | Production | China | 96% |
| REE | Processing | China | 90% |
| Polysilicon | Production | China | 90% |
| Graphite | Production | China | 75% |
| Cobalt | Mining | DR Congo | 68% |
| Nickel | Mining | Indonesia | 50% |

### Current Prices (Feb 2026)
- **Lithium Carbonate:** 134,500 CNY/t (+74% YoY)
- **Cobalt:** $56,290/t (+161% YoY)
- **Nickel:** $17,033/t (+8% YoY)
- **Copper:** $5.85/lb (+28% YoY)

## Project Structure

```
critical-minerals-v2/
├── index.html          # Main dashboard
├── data/
│   ├── minerals.json   # Mineral data (prices, production, reserves)
│   └── supply-chains.json  # Supply chain flow data
├── screenshots/        # Dashboard screenshots
├── DATA_SOURCES.md     # Detailed source documentation
└── README.md           # This file
```

## Data Sources

### Free Public Sources (Used)
- **USGS Mineral Commodity Summaries 2024** — Production, reserves
- **Trading Economics** — Daily prices (CFD-based)
- **LME** — Nickel, cobalt prices
- **Wikipedia** — Production rankings verification

### Paid Sources (For Enhanced Data)
- **Benchmark Mineral Intelligence** — Battery materials ($$$)
- **S&P Global / Platts** — All commodities ($$$)
- **Fastmarkets** — Battery metals ($$$)
- **Asian Metal** — Rare earths, minor metals ($$)

See [DATA_SOURCES.md](DATA_SOURCES.md) for complete source documentation.

## Data Quality Notes

### Excellent Public Data
- Lithium, nickel, copper, cobalt — Good price data from exchanges
- Production/reserves — USGS is authoritative

### Requires Paid Sources
- Real-time rare earth prices (individual elements)
- Battery-grade material specifications
- Gallium/germanium after China export restrictions
- Forward price curves

### Estimates Used
Some data points use industry estimates where public data is unavailable:
- Rare earth individual element prices
- Graphite prices
- Polysilicon prices
- Minor metals (Ga, Ge, Te)

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

Follows [DESIGN_SYSTEM.md](../DESIGN_SYSTEM.md) — Prospector Labs style:
- Dark mode default
- Single accent color (Electric Blue #3B82F6)
- Inter + JetBrains Mono typography
- Horizontal bar charts for rankings
- No gradients, shadows, or decorative elements

## Future Enhancements

- [ ] Add Sankey diagrams for supply chain flows
- [ ] Interactive world map with production/reserves
- [ ] Historical price charts
- [ ] API integration for live prices
- [ ] Export functionality (PNG, PDF)
- [ ] Company-level data drilling

## Credits

**Data:**
- U.S. Geological Survey (USGS)
- Trading Economics
- Industry reports and estimates

**Visualization:**
- Chart.js for charts
- Custom CSS for design system

---

*Built by Prospector Labs — prospectorlabs.io*
