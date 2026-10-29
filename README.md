# 🛒 CommerceLens — Automated E-commerce Analytics & Sentiment

Turn synthetic or authorized commerce CSVs into validated SQL analytics, sentiment summaries and interactive reports.

[Setup](#local-installation--setup-guide) · [Architecture](#architecture--system-design-diagram) · [Detailed guide](PROJECT_GUIDE.md) · [Repository standard](docs/REPOSITORY_STANDARD.md)

## Visuals

![Project hero](<docs/figures/01-commerce-overview.svg>)

Existing project visual; diagrams and illustrative graphics are not evidence of a deployed application.

## Live Link / Demo

Existing published preview link: [Open browser preview](https://harshakavali81-collab.github.io/harshavardhan-portfolio/cases/commercelens.html). This update does not independently verify its availability or backend deployment.

## Key Features

- Deterministic synthetic fixture generation and optional authorized CSV sources.
- Reject invalid prices/ratings/dates; account for discarded/duplicated rows.
- Negation-aware rule sentiment labels: positive, neutral and negative.
- SQLite snapshot with constraints and indexed SQL analytics including window functions.
- Date/category filters, interactive charts, downloadable product comparisons and honest provenance.
- Unit tests and end-to-end CI on every push; three executable notebooks.
- **Ten original SVG project visuals** plus **ten repeatable Matplotlib charts** created from the processed database.

## Tech Stack

![Python](https://img.shields.io/badge/Python-334155?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-334155?style=flat-square) ![Pandas](https://img.shields.io/badge/Pandas-334155?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-334155?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-334155?style=flat-square)

Dependency versions and optional packages are defined in the repository manifests.

## Architecture / System Design Diagram

[Architecture documentation / diagram](<docs/ARCHITECTURE.md>)

## Local Installation & Setup Guide

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

## Challenges & Solutions

**Repository organization:** this project uses `src/`. Keeping those paths stable avoids breaking imports, asset links and deployment commands while the documentation follows a shared format. Project-specific technical limitations and prior release evidence are retained in [Project guide](PROJECT_GUIDE.md).

## Future Improvements

- Capture a reproducible end-to-end demo with runtime versions and sample inputs.
- Expand regression checks for invalid inputs and documented edge cases.
- Record measured results, data provenance and deployment limitations alongside each release.

## Scope and supporting evidence

[](https://github.com/harshakavali81-collab/Automated-E-commerce-Analytics-Sentiment/actions/workflows/ci.yml) [](https://github.com/harshakavali81-collab/Automated-E-commerce-Analytics-Sentiment/actions/workflows/static-site.yml) [](LICENSE)

**Portfolio:** [Full case study](https://harshakavali81-collab.github.io/harshavardhan-portfolio/cases/commercelens.html) · [Interactive synthetic preview](https://harshakavali81-collab.github.io/harshavardhan-portfolio/commercelens-demo.html) · [Download a source-generated static website from CI](https://github.com/harshakavali81-collab/Automated-E-commerce-Analytics-Sentiment/actions/workflows/static-site.yml)

**Python · SQL · Pandas · Streamlit · Plotly · Sentiment · Data quality · CI**



An end-to-end portfolio analytics project: generated or authorized CSV → validated observations → sentiment baseline → SQLite → KPI queries → interactive dashboard → ten exportable data-driven charts.

> **Data provenance:** Default data is fully synthetic (12 fictional products × 120 days = 1,440 product-day observations, plus simulated reviews). Estimated revenue uses synthetic units, not actual customer purchases. Sentiment is not a validated ML accuracy claim. No live retailer integrations or web scraping.

## Repository Structure

| Location | Purpose |
| --- | --- |
| `src/` | Source modules |
| `tests/` | Tests |
| `docs/` | Documentation |
| `data/` | Data and samples |
| `sql/` | SQL schema and analysis |
| `scripts/` | Automation scripts |
| `.github/` | Issue forms, PR template and automated checks |

[Complete file inventory and workflow](docs/REPOSITORY_STANDARD.md). Runtime entry points retain their existing paths.

## Workflow & Tracking

Use the [bug and feature forms](https://github.com/harshakavali81-collab/Automated-E-commerce-Analytics-Sentiment/issues/new/choose) to define work with acceptance criteria. Keep tasks in Todo → In progress → Review → Done, and link a pull request with `Closes #<number>`. See [the maintenance workflow](docs/REPOSITORY_STANDARD.md#workflow).

## License

See [LICENSE](LICENSE) for the existing terms.
