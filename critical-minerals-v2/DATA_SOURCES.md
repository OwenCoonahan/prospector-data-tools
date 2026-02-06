# Data Sources — Critical Minerals Tracker

Last updated: February 6, 2026

## Overview

This document details all data sources used in the Critical Minerals Tracker, including their availability, cost, and reliability.

---

## Primary Data Sources (Free/Public)

### 1. USGS Mineral Commodity Summaries
**URL:** https://pubs.usgs.gov/periodicals/mcs2024/

**Data Available:**
- Annual production by country
- Reserve estimates by country
- Import/export statistics (US)
- Historical production trends
- Major producing mines and companies

**Coverage:**
| Mineral | Production | Reserves | Quality |
|---------|------------|----------|---------|
| Lithium | ✓ Excellent | ✓ Excellent | ⭐⭐⭐⭐⭐ |
| Cobalt | ✓ Good | ✓ Good | ⭐⭐⭐⭐ |
| Nickel | ✓ Excellent | ✓ Excellent | ⭐⭐⭐⭐⭐ |
| Copper | ✓ Excellent | ✓ Excellent | ⭐⭐⭐⭐⭐ |
| Graphite | ✓ Good | ✓ Good | ⭐⭐⭐⭐ |
| Manganese | ✓ Good | ✓ Good | ⭐⭐⭐⭐ |
| Rare Earths | ✓ Good | ✓ Partial | ⭐⭐⭐ |
| Gallium | ✓ Production only | ✗ N/A | ⭐⭐ |
| Germanium | ✓ Production only | ✗ N/A | ⭐⭐ |
| Tellurium | ✓ Production only | ✗ N/A | ⭐⭐ |

**Update Frequency:** Annual (January)
**Cost:** Free


### 2. Trading Economics
**URL:** https://tradingeconomics.com/commodities

**Data Available:**
- Real-time and historical prices
- Price charts
- YoY changes
- Market commentary

**Coverage:**
| Mineral | Real-Time | Historical | Quality |
|---------|-----------|------------|---------|
| Lithium (Carbonate) | ✓ | ✓ | ⭐⭐⭐⭐ |
| Cobalt | ✓ | ✓ | ⭐⭐⭐⭐ |
| Nickel | ✓ | ✓ | ⭐⭐⭐⭐⭐ |
| Copper | ✓ | ✓ | ⭐⭐⭐⭐⭐ |

**Note:** Prices are CFD-based, not spot prices. Good for trends, less reliable for exact contract pricing.

**Update Frequency:** Daily
**Cost:** Free (basic), Paid for API access


### 3. London Metal Exchange (LME)
**URL:** https://www.lme.com/

**Data Available:**
- Official settlement prices
- Warehouse stocks
- Open interest
- Forward curves

**Coverage:**
- Nickel ✓
- Cobalt ✓
- Copper (also COMEX) ✓

**Note:** Full historical data and API access requires subscription.

**Update Frequency:** Daily
**Cost:** Free (delayed), Paid (real-time)


### 4. Wikipedia / Public Sources
**URLs:** 
- https://en.wikipedia.org/wiki/List_of_countries_by_lithium_production
- Related pages for other minerals

**Data Available:**
- Production rankings
- Historical production data
- Source citations

**Quality:** ⭐⭐⭐ (Good for overview, verify with primary sources)

---

## Paid Data Sources (For Real-Time Professional Data)

### 1. Benchmark Mineral Intelligence
**URL:** https://www.benchmarkminerals.com/

**Coverage:**
- Lithium (all forms) ✓✓✓
- Cobalt ✓✓✓
- Nickel (battery grade) ✓✓✓
- Graphite (anode) ✓✓✓
- Rare earths ✓✓

**Data Quality:** ⭐⭐⭐⭐⭐
**Update Frequency:** Weekly/Monthly
**Cost:** $$$$ (Enterprise subscription)


### 2. S&P Global Market Intelligence / Platts
**URL:** https://www.spglobal.com/

**Coverage:**
- All battery metals ✓✓✓
- Rare earths ✓✓
- Supply chain analytics ✓✓✓

**Data Quality:** ⭐⭐⭐⭐⭐
**Cost:** $$$$ (Enterprise subscription)


### 3. Fastmarkets (formerly Metal Bulletin)
**URL:** https://www.fastmarkets.com/

**Coverage:**
- Battery raw materials ✓✓✓
- Cobalt ✓✓✓
- Lithium ✓✓✓
- Nickel ✓✓✓

**Data Quality:** ⭐⭐⭐⭐⭐
**Cost:** $$$$ (Enterprise subscription)


### 4. Asian Metal
**URL:** https://www.asianmetal.com/

**Coverage:**
- Rare earths (detailed) ✓✓✓
- Gallium ✓✓
- Germanium ✓✓
- Minor metals ✓✓✓

**Data Quality:** ⭐⭐⭐⭐
**Cost:** $$ (More affordable than Western sources)


### 5. Shanghai Metals Market (SMM)
**URL:** https://www.metal.com/

**Coverage:**
- China domestic prices ✓✓✓
- Lithium hydroxide/carbonate ✓✓✓
- Battery materials ✓✓✓

**Data Quality:** ⭐⭐⭐⭐
**Cost:** $$$ (Subscription required)

---

## Data by Mineral

### Lithium
| Data Point | Free Source | Paid Source |
|------------|-------------|-------------|
| Price (spot) | Trading Economics (CFD) | Benchmark, Fastmarkets |
| Production | USGS | S&P Global |
| Reserves | USGS | S&P Global |
| Battery-grade specs | ✗ | Benchmark |

### Cobalt
| Data Point | Free Source | Paid Source |
|------------|-------------|-------------|
| Price | LME, Trading Economics | Fastmarkets |
| Production | USGS | S&P Global |
| DRC artisanal data | ✗ | Cobalt Institute |

### Nickel
| Data Point | Free Source | Paid Source |
|------------|-------------|-------------|
| Price | LME, Trading Economics | LME Premium |
| Production | USGS | S&P Global |
| Class 1 vs Class 2 | ✗ | Benchmark |

### Copper
| Data Point | Free Source | Paid Source |
|------------|-------------|-------------|
| Price | COMEX, LME, Trading Economics | Full access |
| Production | USGS | S&P Global |
| Grade premiums | ✗ | Platts |

### Graphite
| Data Point | Free Source | Paid Source |
|------------|-------------|-------------|
| Price | Industry estimates | Benchmark, Fastmarkets |
| Production | USGS | S&P Global |
| Anode-grade specs | ✗ | Benchmark |

### Rare Earth Elements
| Data Point | Free Source | Paid Source |
|------------|-------------|-------------|
| Prices | Industry estimates | Asian Metal, Argus |
| Production | USGS | S&P Global |
| Individual REE | ✗ | Asian Metal |
| Magnet prices | ✗ | Asian Metal |

### Gallium / Germanium
| Data Point | Free Source | Paid Source |
|------------|-------------|-------------|
| Price | Industry estimates only | Asian Metal |
| Production | USGS | Limited |
| China export data | ✗ | Asian Metal |

---

## Data Gaps & Limitations

### Critical Gaps
1. **Real-time rare earth prices** — Requires paid Asian Metal subscription
2. **Gallium/Germanium** — Very limited public data after China export restrictions
3. **Battery-grade specifications** — Benchmark proprietary data
4. **Processing capacity by country** — Industry reports only
5. **Forward curves** — Exchange/paid access only

### Estimates Used
When public data is unavailable, estimates are based on:
- Industry reports (BloombergNEF, IEA)
- Company announcements
- Academic papers
- Historical ratios

### Data Age
- USGS: Annual (data typically 1-2 years old)
- Trading Economics: Daily (prices only)
- Our estimates: Labeled as "est."

---

## Recommended Paid Sources by Use Case

| Use Case | Recommended Source | Cost Tier |
|----------|-------------------|-----------|
| Battery materials research | Benchmark Mineral Intelligence | $$$$ |
| Daily trading | LME/COMEX direct | $$$ |
| Rare earths focus | Asian Metal | $$ |
| General mining intelligence | S&P Global | $$$$ |
| Quick price checks | Trading Economics API | $ |

---

## API Access

### Free APIs
- **Trading Economics:** Limited free tier, paid for more
- **USGS:** No API, PDFs only

### Paid APIs
- **Benchmark:** Enterprise only
- **S&P Global:** Enterprise
- **LME:** DataScope
- **Asian Metal:** Available

---

## Citation Format

When using this data, cite as:
```
Critical Minerals Tracker, Prospector Labs (2026).
Data sources: USGS Mineral Commodity Summaries 2024, 
Trading Economics, industry estimates.
```
