# Repository standard

## Layout

This repository keeps its working source paths. A shared portfolio structure does not require moving a React application, Python package, BI workbook or Verilog project into identical runtime directories.

| Area | Convention |
| --- | --- |
| Landing page | `README.md`: purpose, visuals, demo, features, stack, architecture, setup, tradeoffs and roadmap |
| Detailed reference | `PROJECT_GUIDE.md`: retained project-specific explanation and historical release notes |
| Documentation | `docs/`: design, inventory, reproduction and evidence |
| Work intake | `.github/ISSUE_TEMPLATE/`: bug and feature forms |
| Review | `.github/PULL_REQUEST_TEMPLATE.md`: linked issue, behavior and validation |
| Automation | `.github/workflows/portfolio-docs.yml`: README section and local-link checks |
| Source and tests | Existing project-specific paths listed below; no empty source/test placeholders |

## Workflow

1. Open an issue describing the user problem and measurable acceptance criteria.
2. Add it to a GitHub Project with Todo, In progress, Review and Done states when a board is configured.
3. Use a focused branch and meaningful commits, such as `docs: correct local setup paths` or `fix(api): reject malformed input`.
4. Run the project's documented checks and `python scripts/check_portfolio_docs.py`.
5. Open a pull request with actual validation results and `Closes #<issue-number>`.
6. Merge after review; record release evidence and update the issue/board.

Board creation, profile pins, repository social previews and milestone settings require account-level configuration. This file does not claim those settings have been applied.

## Validation scope

The documentation check validates the landing-page headings and local link targets only. It does not execute models, certify test coverage, inspect Git history for secrets, verify external websites, or prove production readiness. Existing application workflows remain the source of runtime CI evidence.

Keep credentials in local environment variables. A gitignore rule does not remove secrets already tracked or committed. Use only permitted sample data in public demos.

## Inventory at standardization

The following are the pre-existing public project files. New standardization files are described above. Historical guides may mention external bundles that are not part of this list.

- [`Dockerfile`](<../Dockerfile>)
- [`LICENSE`](<../LICENSE>)
- [`Makefile`](<../Makefile>)
- [`README.md`](<../README.md>)
- [`dashboard`](<../dashboard>)
- [`dashboard/app.py`](<../dashboard/app.py>)
- [`data`](<../data>)
- [`data/interim`](<../data/interim>)
- [`data/interim/.gitkeep`](<../data/interim/.gitkeep>)
- [`data/processed`](<../data/processed>)
- [`data/processed/.gitkeep`](<../data/processed/.gitkeep>)
- [`data/raw`](<../data/raw>)
- [`data/raw/.gitkeep`](<../data/raw/.gitkeep>)
- [`docker-compose.yml`](<../docker-compose.yml>)
- [`docs`](<../docs>)
- [`docs/ARCHITECTURE.md`](<../docs/ARCHITECTURE.md>)
- [`docs/CSV_CONTRACTS.md`](<../docs/CSV_CONTRACTS.md>)
- [`docs/DATA_DICTIONARY.md`](<../docs/DATA_DICTIONARY.md>)
- [`docs/DATA_LINEAGE.md`](<../docs/DATA_LINEAGE.md>)
- [`docs/DEPLOYMENT.md`](<../docs/DEPLOYMENT.md>)
- [`docs/ERD.md`](<../docs/ERD.md>)
- [`docs/INTERVIEW_NOTES.md`](<../docs/INTERVIEW_NOTES.md>)
- [`docs/OPERATIONS.md`](<../docs/OPERATIONS.md>)
- [`docs/PORTFOLIO_CASE_STUDY.md`](<../docs/PORTFOLIO_CASE_STUDY.md>)
- [`docs/PORTFOLIO_RECRUITER_SUMMARY.md`](<../docs/PORTFOLIO_RECRUITER_SUMMARY.md>)
- [`docs/PROJECT_TREE.txt`](<../docs/PROJECT_TREE.txt>)
- [`docs/SECURITY.md`](<../docs/SECURITY.md>)
- [`docs/SENTIMENT_MODEL_CARD.md`](<../docs/SENTIMENT_MODEL_CARD.md>)
- [`docs/STATIC_HOSTING.md`](<../docs/STATIC_HOSTING.md>)
- [`docs/VALIDATION.md`](<../docs/VALIDATION.md>)
- [`docs/figures`](<../docs/figures>)
- [`docs/figures/01-commerce-overview.svg`](<../docs/figures/01-commerce-overview.svg>)
- [`docs/figures/02-data-pipeline.svg`](<../docs/figures/02-data-pipeline.svg>)
- [`docs/figures/03-price-trend.svg`](<../docs/figures/03-price-trend.svg>)
- [`docs/figures/04-category-revenue.svg`](<../docs/figures/04-category-revenue.svg>)
- [`docs/figures/05-sentiment-mix.svg`](<../docs/figures/05-sentiment-mix.svg>)
- [`docs/figures/06-rating-bars.svg`](<../docs/figures/06-rating-bars.svg>)
- [`docs/figures/07-discount-comparison.svg`](<../docs/figures/07-discount-comparison.svg>)
- [`docs/figures/08-inventory-health.svg`](<../docs/figures/08-inventory-health.svg>)
- [`docs/figures/09-product-comparison.svg`](<../docs/figures/09-product-comparison.svg>)
- [`docs/figures/10-quality-monitor.svg`](<../docs/figures/10-quality-monitor.svg>)
- [`notebooks`](<../notebooks>)
- [`notebooks/01_data_quality.ipynb`](<../notebooks/01_data_quality.ipynb>)
- [`notebooks/02_price_eda.ipynb`](<../notebooks/02_price_eda.ipynb>)
- [`notebooks/03_sentiment_analysis.ipynb`](<../notebooks/03_sentiment_analysis.ipynb>)
- [`requirements.txt`](<../requirements.txt>)
- [`scripts`](<../scripts>)
- [`scripts/__init__.py`](<../scripts/__init__.py>)
- [`scripts/build_report.py`](<../scripts/build_report.py>)
- [`scripts/build_site.py`](<../scripts/build_site.py>)
- [`scripts/refresh.py`](<../scripts/refresh.py>)
- [`sql`](<../sql>)
- [`sql/advanced_analytics.sql`](<../sql/advanced_analytics.sql>)
- [`sql/kpis.sql`](<../sql/kpis.sql>)
- [`sql/schema.sql`](<../sql/schema.sql>)
- [`src`](<../src>)
- [`src/__init__.py`](<../src/__init__.py>)
- [`src/analytics`](<../src/analytics>)
- [`src/analytics/__init__.py`](<../src/analytics/__init__.py>)
- [`src/analytics/alerts.py`](<../src/analytics/alerts.py>)
- [`src/analytics/charts.py`](<../src/analytics/charts.py>)
- [`src/analytics/metrics.py`](<../src/analytics/metrics.py>)
- [`src/analytics/report.py`](<../src/analytics/report.py>)
- [`src/ingestion`](<../src/ingestion>)
- [`src/ingestion/__init__.py`](<../src/ingestion/__init__.py>)
- [`src/ingestion/generate_demo.py`](<../src/ingestion/generate_demo.py>)
- [`src/ingestion/load_csv.py`](<../src/ingestion/load_csv.py>)
- [`src/pipeline`](<../src/pipeline>)
- [`src/pipeline/__init__.py`](<../src/pipeline/__init__.py>)
- [`src/pipeline/run.py`](<../src/pipeline/run.py>)
- [`src/processing`](<../src/processing>)
- [`src/processing/__init__.py`](<../src/processing/__init__.py>)
- [`src/processing/clean.py`](<../src/processing/clean.py>)
- [`src/processing/export.py`](<../src/processing/export.py>)
- [`src/sentiment`](<../src/sentiment>)
- [`src/sentiment/__init__.py`](<../src/sentiment/__init__.py>)
- [`src/sentiment/lexicon.py`](<../src/sentiment/lexicon.py>)
- [`tests`](<../tests>)
- [`tests/test_advanced.py`](<../tests/test_advanced.py>)
- [`tests/test_contracts.py`](<../tests/test_contracts.py>)
- [`tests/test_pipeline.py`](<../tests/test_pipeline.py>)
- [`tests/test_quality.py`](<../tests/test_quality.py>)
- [`tests/test_sentiment.py`](<../tests/test_sentiment.py>)
- [`tests/test_sql_advanced.py`](<../tests/test_sql_advanced.py>)
- [`tests/test_static_site.py`](<../tests/test_static_site.py>)
