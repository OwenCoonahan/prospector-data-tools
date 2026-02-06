# Live Data Sources — Grid Stress Monitor

This document catalogs real-time data availability from US ISOs for the Grid Stress Monitor dashboard.

---

## Summary Table

| ISO | LMP Data | Grid Status | Fuel Mix | Auth | Update Freq | Status |
|-----|----------|-------------|----------|------|-------------|--------|
| **ERCOT** | ✅ Public | ✅ Public | ✅ Public | None | 5 min | **INTEGRATED** |
| **EIA** | ❌ | ✅ Demand | ❌ | Demo key works | Hourly | Partial |
| **CAISO** | 🔒 OASIS | ⚠️ Outlook | ❌ | Requires OASIS account | 5 min | Not accessible |
| **PJM** | 🔒 Data Miner | ⚠️ Limited | ⚠️ | API key required | 5 min | Not accessible |
| **MISO** | ⚠️ Changed | ✅ Public | ❌ | None | 5 min | Investigating |
| **NYISO** | 🔒 | ⚠️ Dashboard | ❌ | Unknown | 5 min | Not accessible |
| **SPP** | 🔒 | ⚠️ | ❌ | Unknown | 5 min | Not accessible |
| **ISONE** | 🔒 | ⚠️ | ❌ | Unknown | 5 min | Not accessible |

---

## ERCOT — **PRIMARY SOURCE** ✅

ERCOT provides excellent public JSON APIs with no authentication required.

### Available Endpoints

#### 1. Real-Time LMPs (Hub & Load Zones)
```
URL: https://www.ercot.com/content/cdr/html/hb_lz.html
Format: HTML table (parseable)
Update: Every 5 minutes
Auth: None
```

Sample zones:
- `HB_HOUSTON`, `HB_NORTH`, `HB_SOUTH`, `HB_WEST`, `HB_PAN`
- `LZ_HOUSTON`, `LZ_NORTH`, `LZ_SOUTH`, `LZ_WEST`, `LZ_CPS`, `LZ_LCRA`

#### 2. Real-Time LMPs (All Settlement Points)
```
URL: https://www.ercot.com/content/cdr/html/current_np6788.html
Format: HTML table (parseable)  
Update: Every 5 minutes
Auth: None
```

Returns 900+ settlement points with individual LMPs.

#### 3. Fuel Mix by Type
```
URL: https://www.ercot.com/api/1/services/read/dashboards/fuel-mix.json
Format: JSON
Update: Every 5 minutes
Auth: None
```

Response structure:
```json
{
  "lastUpdated": "2026-02-06 09:31:00-0600",
  "monthlyCapacity": {
    "Coal and Lignite": 13705,
    "Natural Gas": 68441,
    "Nuclear": 5268,
    "Solar": 36437,
    "Wind": 40588,
    "Power Storage": 16866,
    "Hydro": 579,
    "Other": 667
  },
  "data": {
    "2026-02-06": {
      "<timestamp>": {
        "Wind": {"gen": 5950.07},
        "Solar": {"gen": 0.38},
        "Natural Gas": {"gen": 29157.90},
        ...
      }
    }
  }
}
```

#### 4. Supply & Demand
```
URL: https://www.ercot.com/api/1/services/read/dashboards/supply-demand.json
Format: JSON
Update: Every 5 minutes
Auth: None
```

Response structure:
```json
{
  "lastUpdated": "2026-02-06 09:30:00-0600",
  "data": [
    {
      "capacity": 67673,
      "demand": 46918,
      "timestamp": "2026-02-06 00:00:00-0600",
      "hourEnding": 0
    }
  ]
}
```

### ERCOT Zone Coordinates

| Zone | Lat | Lng | Description |
|------|-----|-----|-------------|
| HB_HOUSTON | 29.76 | -95.37 | Houston hub |
| HB_NORTH | 32.78 | -96.80 | Dallas/North Texas |
| HB_SOUTH | 27.80 | -97.40 | Corpus Christi area |
| HB_WEST | 31.76 | -106.49 | El Paso/West Texas |
| HB_PAN | 35.22 | -101.83 | Panhandle (wind corridor) |
| LZ_CPS | 29.42 | -98.49 | San Antonio |
| LZ_LCRA | 30.27 | -97.74 | Austin/LCRA |

---

## EIA API — Hourly Grid Data

The US Energy Information Administration provides hourly demand data for all ISOs.

### Endpoint
```
URL: https://api.eia.gov/v2/electricity/rto/region-data/data/
Auth: API key (DEMO_KEY works for limited use)
Format: JSON
Update: Hourly
```

### Parameters
- `frequency=hourly`
- `data[0]=value`
- `facets[respondent][]=ERCO` (or CISO, PJM, MISO, etc.)
- `facets[type][]=D` (Demand) or `NG` (Net Generation)

### Example Request
```
https://api.eia.gov/v2/electricity/rto/region-data/data/?api_key=DEMO_KEY&frequency=hourly&data[0]=value&facets[respondent][]=ERCO&facets[type][]=D&length=24
```

### Response
```json
{
  "response": {
    "data": [
      {
        "period": "2026-02-06T14",
        "respondent": "ERCO",
        "type": "D",
        "value": "55094",
        "value-units": "megawatthours"
      }
    ]
  }
}
```

### Available Respondents (ISOs)
- `ERCO` — ERCOT
- `CISO` — CAISO
- `PJM` — PJM
- `MISO` — MISO
- `SWPP` — SPP
- `NYIS` — NYISO
- `ISNE` — ISO-NE

---

## CAISO — California ISO

### OASIS (Official)
```
URL: http://oasis.caiso.com/oasisapi/
Auth: Requires OASIS account registration
Format: XML/ZIP
```

OASIS requires registration and returns data in zip-compressed XML format.

### Today's Outlook (Web)
```
URL: https://www.caiso.com/todays-outlook/prices
```
Data is rendered client-side via JavaScript. Not directly accessible via fetch.

**Status:** Not accessible without browser automation or OASIS account.

---

## MISO — Midcontinent ISO

### New API (December 2025)
MISO transitioned to JSON-only APIs in December 2025.

```
Previous: https://api.misoenergy.org/MISORTWDDataBroker/DataBrokerServices.asmx
New: Unknown endpoint structure
Docs: https://www.misoenergy.org/markets-and-operations/rtdataapis
```

Their documentation states:
> "Please be respectful of caching limits and avoid accessing these links more than once per minute."

**Status:** Investigating new API structure.

---

## PJM — PJM Interconnection

### Data Miner
```
URL: https://dataminer2.pjm.com/
Auth: API key required (free registration)
Format: JSON
```

PJM requires registration for API access. Provides:
- LMPs at various nodes
- Load forecasts
- Generation by fuel type

**Status:** Requires API key registration.

---

## NYISO — New York ISO

### Dashboard
```
URL: https://www.nyiso.com/real-time-dashboard
```
Dashboard renders via JavaScript. Zone maps available as PDFs.

**Status:** Not directly accessible via API.

---

## Implementation Status

### Currently Integrated
1. **ERCOT Real-Time LMPs** — 5-minute updates for hubs and zones
2. **ERCOT Fuel Mix** — Generation by source type
3. **ERCOT Supply/Demand** — System-wide capacity vs demand

### Fallback Mode
When live data is unavailable:
- Dashboard shows "SAMPLE DATA" indicator
- Uses realistic sample data based on typical patterns
- Explains what live data would show

### Planned
1. EIA hourly demand for cross-ISO comparison
2. MISO integration (pending API investigation)
3. PJM integration (pending API key)

---

## Rate Limits & Best Practices

| Source | Rate Limit | Cache Duration |
|--------|------------|----------------|
| ERCOT | No explicit limit | 5 minutes |
| EIA | ~1000/hour (demo key) | 1 hour |
| MISO | 1 request/minute | 1 minute |

### Recommendations
1. Cache responses for their update frequency
2. Show "last updated" timestamp
3. Implement exponential backoff on failures
4. Don't poll faster than data updates

---

## CORS Notes

All ERCOT endpoints return proper CORS headers. Direct browser fetch works.
EIA API allows CORS.
Other ISOs may require a proxy server for browser-based access.

---

*Last updated: 2026-02-06*
