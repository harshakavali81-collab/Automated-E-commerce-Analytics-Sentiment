# Data provenance and lineage

1. **Generator**: src/ingestion/generate_demo.py emits deterministic fictional prices.csv and reviews.csv with a fixed random seed of 42 by default. Product identities and review snippets are invented. Dates begin 2026-01-01.
2. **Optional authorized import**: two CSVs may be supplied through explicit local file paths. The program does not check whether the user truly has rights to process those files; that remains the user's responsibility.
3. **Cleaning**: parsing, date and number checks, duplicate counts, valid price product IDs in reviews. Invalid rows are rejected and recorded in summary.json.
4. **Transform**: English lexicon-based sentiment label for each accepted review. Ratings are kept independent from sentiment labels.
5. **Storage**: prices and reviews stored in SQLite with explicit constraints and indexes. Each refresh replaces the whole prior snapshot transactionally.
6. **Derived outputs**: summary.json, alerts.json, SQL KPIs, a Streamlit interface, optional Matplotlib PNGs, and offline ten-chart HTML report.
7. **Data limitations**: The prototype has one price observation per product/date and does not preserve multiple merchants for a product on a single day.

Default expected price observations = 12 products × 120 days = 1,440. Default review count depends on the deterministic generator's cadence. No actual revenue, completed transactions, licensed marketplace feeds or customer review volume is claimed.

## Reproducibility
Run python -m scripts.refresh --demo to regenerate the entire demonstration. Run python -m unittest discover -s tests -v for input contract and regression checks.

## Retention
Raw data, intermediate outputs, processed SQLite and exported reports are intentionally excluded from Git by .gitignore. Verify ignore state and avoid forced-add or other accidental public exposure. Backups and deletion practices for real licensed files must be defined by the organization handling them.
