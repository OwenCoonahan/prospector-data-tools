# Grid Supply Chain Intelligence

**Comprehensive resource for electrical grid infrastructure sourcing**

A centralized intelligence tool for anyone sourcing grid infrastructure components — covering manufacturers, lead times, materials, and supply chain constraints.

## Live Demo

Open `index.html` in a browser to explore the interactive visualization.

## What's Covered

### Components (7 Categories)

1. **Large Power Transformers (LPT)** — 100+ MVA transmission transformers
2. **Distribution Transformers** — <10 MVA for end-use delivery
3. **High Voltage Bushings** — Critical transformer components
4. **Switchgear** — GIS (gas-insulated) and AIS (air-insulated)
5. **Circuit Breakers** — HV protection devices
6. **Cables & Conductors** — HVDC, XLPE, overhead lines
7. **Insulators** — Porcelain and composite

### Critical Materials

- **Grain-Oriented Electrical Steel (GOES)** — Transformer cores (70% US import dependent)
- **Copper** — Windings and conductors
- **Transformer Oil** — Insulation and cooling
- **Aluminum** — Overhead conductors
- **SF6 Gas** — Switchgear insulation (regulatory pressure)
- **Porcelain/Composite** — Insulators

### Manufacturers Tracked (14+)

| Manufacturer | HQ | US Market Share | Key Products |
|-------------|-----|-----------------|--------------|
| Hitachi Energy | 🇨🇭 Switzerland | ~20% | LPT, HVDC, GIS |
| Siemens Energy | 🇩🇪 Germany | ~15% | LPT, GIS, Breakers |
| GE Vernova | 🇺🇸 USA | ~14% | LPT, Distribution |
| Hyundai Electric | 🇰🇷 South Korea | ~6% | LPT (new US plant 2025) |
| Virginia Transformer | 🇺🇸 USA | ~8% | LPT, Medium Power |
| Howard Industries | 🇺🇸 USA | ~20% (dist) | Distribution |
| Prolec GE | 🇲🇽 Mexico | ~10% | LPT, Distribution |
| SPX Transformer | 🇺🇸 USA | ~3% | LPT, Mobile |
| + 6 more... | | | |

## Current Lead Times (Feb 2026)

| Equipment | Pre-2020 | Peak 2023 | Current |
|-----------|----------|-----------|---------|
| Large Power Transformers | 12-18 mo | 36-60 mo | 28-42 mo |
| GSU Transformers | 18-24 mo | 48-72 mo | 36-48 mo |
| Distribution Transformers | 2-6 mo | 12-24 mo | 8-14 mo |
| GIS Switchgear | 12-20 mo | 24-36 mo | 18-30 mo |
| HV Circuit Breakers | 8-16 mo | 18-30 mo | 14-26 mo |
| HVDC Cables | 24-48 mo | 36-60 mo | 32-52 mo |

**Outlook:** Lead times improving but still 2-2.5x pre-pandemic. Normalization not expected before 2027-2028.

## Data Structure

```
data/
├── manufacturers.json   # 14+ manufacturer profiles
├── components.json      # 11 component types with specs
├── materials.json       # 8 critical materials with supply chain
├── lead-times.json      # Historical and current lead times
└── news.json            # Recent industry news/insights
```

## Key Insights

1. **GOES Steel** is the critical bottleneck — Cleveland-Cliffs is the only US producer
2. **Only ~6 US facilities** can manufacture large power transformers
3. **2,600 GW** in US interconnection queue, each project needs transformers
4. **Data center demand** exceeding forecasts by 2-3x
5. **Capacity expansion** underway (Hyundai AL, Hitachi Sweden, Virginia Transformer)
6. **SF6 regulations** driving switchgear innovation

## Sources

See [SOURCES.md](SOURCES.md) for full methodology and data sources including:
- DOE reports and programs
- Utility IRP filings
- NERC reliability assessments
- Industry publications (T&D World, Power Engineering)
- Manufacturer press releases
- Trade data

## Design

Built following [DESIGN_SYSTEM.md](../../DESIGN_SYSTEM.md):
- Dark mode (Charcoal background)
- Geist font family
- Horizontal bar charts
- Single accent color (Electric blue)
- Mobile responsive

## Disclaimer

This data is compiled from public sources and estimates. Lead times and market shares are approximate and vary by specification, relationship, and market conditions. Users should verify critical data points directly with manufacturers before making procurement decisions.

---

*prospectorlabs.io — Grid Supply Chain Intelligence — February 2026*
