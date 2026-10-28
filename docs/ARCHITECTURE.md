# Architecture and workflow

Synthetic generator OR authorized CSV → schema validation → deduplicate → negation-aware sentiment → SQLite → SQL KPIs + JSON data quality → Streamlit dashboard and chart exports.

The Python standard library powers the core pipeline. SQLite is refreshed transactionally. Key price uniqueness is product_id plus observed_date, so multiple sellers on the same product/day are not preserved: seller-aware modeling is future work. No scraping or real-time retailer API is configured. No externally validated sentiment classifier is implemented.

## Extended architecture

- One-shot offline refresh command prepares database, alerts JSON and self-contained ten-chart HTML report.
- Day-on-day movement flags use SQLite LAG and configurable percent thresholds; latest low-stock flags use ROW_NUMBER.
- Docker and Compose permit reproducible localhost dashboard runtime, without pretending to provide a real-data public SaaS.
- Three CI jobs: core Python and report checks; dependency-enabled UI/chart checks; container startup/health checks.
- All production boundaries and privacy requirements are in SECURITY.md and OPERATIONS.md.
