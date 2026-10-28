# 🛒 CommerceLens — Automated E-commerce Analytics & Sentiment

**Python · SQL · Pandas · Streamlit · Plotly · Sentiment · Data quality · CI**

![Project hero](docs/figures/01-commerce-overview.svg)

An end-to-end portfolio analytics project: generated or authorized CSV → validated observations → sentiment baseline → SQLite → KPI queries → interactive dashboard → ten exportable data-driven charts.

> **Data provenance:** Default data is fully synthetic (12 fictional products × 120 days = 1,440 product-day observations, plus simulated reviews). Estimated revenue uses synthetic units, not actual customer purchases. Sentiment is not a validated ML accuracy claim. No live retailer integrations or web scraping.

## Workflow
```mermaid
flowchart LR
 A[Synthetic or authorized CSV] --> B[Quality checks and dedup]
 B --> C[Review sentiment baseline]
 C --> D[(SQLite)]
 D --> E[SQL KPIs and quality JSON]
 E --> F[Streamlit dashboard]
 D --> G[10 generated graphs]
 H[Automated tests] --> B
```

## Quick start
```bash
git clone https://github.com/harshakavali81-collab/Automated-E-commerce-Analytics-Sentiment.git
cd Automated-E-commerce-Analytics-Sentiment
python -m unittest discover -s tests -v
python -m src.pipeline.run --demo
python -m pip install -r requirements.txt
streamlit run dashboard/app.py
python -m src.analytics.charts
```

To import licensed CSVs (columns in data dictionary):
```bash
python -m src.pipeline.run --prices /path/prices.csv --reviews /path/reviews.csv
```

## Features
- Deterministic synthetic fixture generation and optional authorized CSV sources.
- Reject invalid prices/ratings/dates; account for discarded/duplicated rows.
- Negation-aware rule sentiment labels: positive, neutral and negative.
- SQLite snapshot with constraints and indexed SQL analytics including window functions.
- Date/category filters, interactive charts, downloadable product comparisons and honest provenance.
- Unit tests and end-to-end CI on every push; three executable notebooks.
- **Ten original SVG project visuals** plus **ten repeatable Matplotlib charts** created from the processed database.

## Gallery — 10 illustrations (NOT externally measured retail data)

| Illustration | Illustration |
|---|---|
| ![Commerce overview](docs/figures/01-commerce-overview.svg) | ![Data pipeline](docs/figures/02-data-pipeline.svg) |
| ![Price trend](docs/figures/03-price-trend.svg) | ![Revenue comparison](docs/figures/04-category-revenue.svg) |
| ![Sentiment mix](docs/figures/05-sentiment-mix.svg) | ![Rating analysis](docs/figures/06-rating-bars.svg) |
| ![Discount trends](docs/figures/07-discount-comparison.svg) | ![Inventory health](docs/figures/08-inventory-health.svg) |
| ![Product rankings](docs/figures/09-product-comparison.svg) | ![Quality controls](docs/figures/10-quality-monitor.svg) |

## Technical documentation
[Architecture](docs/ARCHITECTURE.md) · [Data dictionary](docs/DATA_DICTIONARY.md) · [Validation](docs/VALIDATION.md) · [Deployment](docs/DEPLOYMENT.md) · [Portfolio case study](docs/PORTFOLIO_CASE_STUDY.md) · [Tree](docs/PROJECT_TREE.txt) · [SQL KPIs](sql/kpis.sql)

## Further evidence
[Sentiment model card](docs/SENTIMENT_MODEL_CARD.md) · [Data lineage](docs/DATA_LINEAGE.md) · [Recruiter project summary](docs/PORTFOLIO_RECRUITER_SUMMARY.md) · [Latest workflow results](https://github.com/harshakavali81-collab/Automated-E-commerce-Analytics-Sentiment/actions/workflows/ci.yml)

## Scope and known limitations
Default prices, units and reviews are synthetic; this does not demonstrate measured revenue, sentiment prediction accuracy, real-time refresh or market scraping. A public Streamlit deployment and genuine authorized retailer feed are **not configured**. Imported third-party data require permission, privacy review and source verification.

## Extended delivery: offline report, alerts and local Docker

The enhanced project includes a complete **one-command synthetic data refresh** that produces a constrained SQLite snapshot, an alerts JSON file and a **standalone HTML report with 10 actual data-driven inline SVG charts** (distinct from the 10 illustrative README gallery images).

~~~bash
python -m scripts.refresh --demo
# Open reports/commerce.html in Chrome, Edge or Firefox (no web server needed).
~~~

The price-change rule flags consecutive observations moving at least 15%; the stock rule flags latest inventory at or below 10 units. These are heuristics on synthetic/default or supplied data and are not proven market-alert performance.

### Local Docker run

~~~bash
docker compose up --build -d
# Open http://127.0.0.1:8501
docker compose logs --tail=50
docker compose down
~~~

The Docker demo binds to **localhost only**, runs the app as a non-root user, and generates fictional records at startup. Docker packaging does not imply a public production deployment.

### Reproducible quality evidence

GitHub Actions now checks unit and integration tests, the source-driven offline report, dashboard dependencies and Streamlit rendering, all 10 Matplotlib chart exports, and a container build/service health check. Monitor the Actions page for pass/fail status before describing these checks as passed.

[Advanced SQL](sql/advanced_analytics.sql) · [Architecture and data contracts](docs/ARCHITECTURE.md) · [Security and privacy](docs/SECURITY.md) · [Runbook](docs/OPERATIONS.md) · [ER model](docs/ERD.md) · [Interview walkthrough](docs/INTERVIEW_NOTES.md)

**Limits still requiring actual services:** live licensed retailer API feeds, independent sentiment quality validation, production hosting and real customer/business outcomes. No credentials or real customer data have been used.
