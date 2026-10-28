# Operations and local deployment

## Python setup

Requires Python 3.11 or later.

~~~bash
python -m unittest discover -s tests -v
python -m scripts.refresh --demo
python -m pip install -r requirements.txt
streamlit run dashboard/app.py
python -m src.analytics.charts
~~~

The refresh creates a SQLite snapshot, alerts JSON and reports/commerce.html with ten snapshot-derived SVG charts. You can open reports/commerce.html directly in Chrome, Edge or Firefox with no internet connection. The charts created by Matplotlib are an additional output.

## Docker Compose

~~~bash
docker compose up --build -d
docker compose ps
docker compose logs --tail=100
docker compose down
~~~

Local dashboard: http://127.0.0.1:8501

The container automatically generates SYNTHETIC data on startup, runs as non-root, and stores outputs in named local Docker volumes. It does not deploy anything to a public cloud.

## Authorized CSV refresh

~~~bash
python -m scripts.refresh --prices /safe/prices.csv --reviews /safe/reviews.csv
~~~

Only use licensed data and understand the documented input schema. Optional scheduled execution can invoke this command through a locally configured cron job or Windows Task Scheduler. There is no working external API feed, remote refresh job, or claim of live prices.

## Routine checks
Review data/processed/summary.json for rejection/duplicate counts. Review data/processed/alerts.json for flagged day-on-day observations and latest stock proxies. These are rule-based heuristics, not verified trading, sourcing or inventory recommendations.

## Failure recovery
For purely synthetic data, re-run the generator using --demo. For a licensed dataset, secure a private backup of originals before rebuilding. Do not commit reports or source CSVs containing customer data.
