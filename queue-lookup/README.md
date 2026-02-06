# Queue Lookup

**US Interconnection Queue Search Tool**

A fast, client-side search interface for exploring 35,000+ US interconnection queue projects across all major ISOs.

## Features

- **Full-text search** — Search by project name, developer, queue ID, or POI
- **Multi-filter** — Filter by region, type, status, state, and minimum capacity
- **Sortable columns** — Click any header to sort
- **Dark/Light mode** — Respects system preference, toggleable
- **Zero backend** — Pure client-side, deploys anywhere (GitHub Pages, S3, etc.)
- **Fast** — Debounced search, paginated results

## Data

- **35,469 projects** from public ISO queues
- **6.3+ TW** total capacity
- **9 regions**: MISO, PJM, ERCOT, CAISO, SPP, West, ISO-NE, NYISO, Southeast
- Updated: Feb 2026

## Stack

- Vanilla HTML/CSS/JS (no frameworks)
- Outfit + JetBrains Mono fonts
- ~6.6MB JSON data file (gzips to ~1.5MB)

## Deploy

```bash
# Local dev
python3 -m http.server 8000

# GitHub Pages
git push origin main  # with Pages enabled

# Any static host
# Just upload the folder
```

## Project Structure

```
queue-lookup/
├── index.html          # Single-file app
├── data/
│   ├── projects.json   # Full export (6.8MB)
│   └── projects.min.json # Minified (6.6MB)
├── screenshots/
│   ├── light-loaded.png
│   └── dark-loaded.png
└── README.md
```

## License

MIT — Built by [Prospector Labs](https://prospectorlabs.io)
