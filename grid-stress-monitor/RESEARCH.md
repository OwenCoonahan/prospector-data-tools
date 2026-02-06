# Grid Stress Monitor - Data Research

## Executive Summary

Grid stress and congestion data is available from multiple sources. The best approach is a combination of ISO-direct APIs and aggregator services. **gridstatus.io** provides the most unified access, but direct ISO APIs work for MVP.

---

## Data Sources by Type

### 1. LMP (Locational Marginal Pricing) Data

LMPs reveal congestion—when prices diverge significantly between locations, it indicates transmission constraints.

| ISO | Data Product | Frequency | Access |
|-----|-------------|-----------|--------|
| **ERCOT** | NP6-788-CD (Real-Time LMPs by Settlement Point) | 5-min | Public API |
| **ERCOT** | NP6-970-CD (Indicative LMPs) | 5-min | Public API |
| **PJM** | rt_hrl_lmps (Real-Time Hourly LMPs) | Hourly | Data Miner 2 |
| **CAISO** | OASIS LMP | 5-min | OASIS API |
| **MISO** | RT LMP | 5-min | MISOftp |
| **NYISO** | RT LBMP | 5-min | OASIS |
| **SPP** | LMP | 5-min | Market Portal |
| **ISO-NE** | Five Minute LMPs | 5-min | ISO Express |

**Key Insight:** High LMP spreads (>$50/MWh between zones) indicate congestion.

### 2. Transmission Constraint Data

| ISO | Data Source | Notes |
|-----|-------------|-------|
| **ERCOT** | SCED Shadow Prices | Available via market reports |
| **PJM** | Constraint Documents | Explicit constraint postings |
| **CAISO** | Transmission Constraint Relaxation | OASIS |
| **MISO** | Binding Constraints | Market reports |

### 3. Curtailment Data (Wind/Solar)

| ISO | Data Source | Notes |
|-----|-------------|-------|
| **ERCOT** | Wind/Solar Actual vs Forecast | Shows economic curtailment |
| **CAISO** | Curtailment Reports | Explicit curtailment data |
| **SPP** | Wind Curtailment | Major wind curtailment region |

### 4. Emergency Alerts / Grid Warnings

| ISO | Alert Types |
|-----|-------------|
| **ERCOT** | Energy Emergency Alerts (EEA1, EEA2, EEA3), Operating Condition Notices |
| **PJM** | Emergency Procedures, Load Management |
| **CAISO** | Flex Alerts, Emergency Notifications |
| **MISO** | Maximum Generation Events |

### 5. Historical Outage Data

- **EIA Form 861**: Annual outage statistics
- **FERC Form 714**: Annual demand and reliability
- **DOE OE-417**: Major disturbance reports

---

## Aggregator Services

### gridstatus.io (Python library + hosted API)
- **Pros:** Unified API across all ISOs, clean data
- **Cons:** Some endpoints require API key for production use
- **Python:** `pip install gridstatus`
- **Supports:** CAISO, SPP, ISONE, MISO, ERCOT, NYISO, PJM

### EIA Open Data API
- **URL:** https://api.eia.gov/
- **Requires:** Free API key registration
- **Data:** Demand, generation, interchange by region

---

## ISO Geographic Boundaries

| ISO | Coverage | Key Zones |
|-----|----------|-----------|
| **ERCOT** | Texas (isolated grid) | Houston, North, South, West, Load Zones |
| **PJM** | Mid-Atlantic + Midwest (13 states) | COMED, AEP, PECO, BGE, DOM, etc. |
| **CAISO** | California | NP15, SP15, ZP26 |
| **MISO** | Central US (15 states) | Zone 1-11 |
| **SPP** | Great Plains (14 states) | Multiple pricing nodes |
| **NYISO** | New York State | Zones A-K (West to Long Island) |
| **ISO-NE** | New England (6 states) | CT, ME, NH, RI, VT, SEMA, WCMA, NEMA |

---

## Data Used in This MVP

For the Grid Stress Monitor MVP, we use:

1. **LMP Data (Real-Time)** - ERCOT and PJM zones
2. **Congestion indicators** - LMP spread calculations
3. **Zone boundaries** - GeoJSON approximations
4. **Historical patterns** - Sample data showing stress scenarios

---

## API Endpoints (Direct Access)

### ERCOT Public API
```
Base: https://www.ercot.com/api/1/services/read/
Example: /dashboards/todays-outlook.json
```
*Note: Protected by Incapsula, may need browser-based fetching*

### PJM Data Miner 2
```
Base: https://api.pjm.com/api/v1/
Docs: https://dataminer2.pjm.com/
Auth: API key required for some endpoints
```

### CAISO OASIS
```
Base: http://oasis.caiso.com/oasisapi/
Example: SingleZip?queryname=PRC_LMP&...
```

---

## Recommended Approach

1. **MVP:** Use sample data based on real ISO data structures
2. **V2:** Integrate gridstatus Python library for live data
3. **V3:** Set up scheduled data pulls with caching

---

## References

- gridstatus docs: https://opensource.gridstatus.io/
- ERCOT Data Products: https://www.ercot.com/mp/data-products
- PJM Data Miner: https://dataminer2.pjm.com/
- CAISO OASIS: http://oasis.caiso.com/
- EIA OpenData: https://www.eia.gov/opendata/
