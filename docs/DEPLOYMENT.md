# Run locally

Python 3.11 or later:

    python -m unittest discover -s tests -v
    python -m src.pipeline.run --demo
    python -m pip install -r requirements.txt
    streamlit run dashboard/app.py
    python -m src.analytics.charts

Charts are generated under docs/generated-charts from the local SQLite snapshot. To use licensed files, run python -m src.pipeline.run --prices /path/prices.csv --reviews /path/reviews.csv.

GitHub Actions tests use only fictional data. No hosted Streamlit service, external-source scheduler, access control or real-time ingestion is deployed.
