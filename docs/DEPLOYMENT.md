# Run locally

Python 3.11 or later:

    python -m unittest discover -s tests -v
    python -m src.pipeline.run --demo
    python -m pip install -r requirements.txt
    streamlit run dashboard/app.py
    python -m src.analytics.charts

Charts are generated under docs/generated-charts from the local SQLite snapshot. To use licensed files, run python -m src.pipeline.run --prices /path/prices.csv --reviews /path/reviews.csv.

GitHub Actions tests use only fictional data. No hosted Streamlit service, external-source scheduler, access control or real-time ingestion is deployed.

## Faster offline demo

~~~bash
python -m scripts.refresh --demo
# Then open reports/commerce.html in any current browser.
~~~

## Optional local Docker container

~~~bash
docker compose up --build -d
# Streamlit at http://127.0.0.1:8501
docker compose down
~~~

The Compose port is bound to localhost by default. Do not assume the repository or Docker container is a remotely accessible production web service. See docs/OPERATIONS.md and docs/SECURITY.md.
