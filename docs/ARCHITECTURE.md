# Architecture and workflow

Synthetic generator OR authorized CSV → schema validation → deduplicate → negation-aware sentiment → SQLite → SQL KPIs + JSON data quality → Streamlit dashboard and chart exports.

The Python standard library powers the core pipeline. SQLite is refreshed transactionally. Key price uniqueness is product_id plus observed_date, so multiple sellers on the same product/day are not preserved: seller-aware modeling is future work. No scraping or real-time retailer API is configured. No externally validated sentiment classifier is implemented.
