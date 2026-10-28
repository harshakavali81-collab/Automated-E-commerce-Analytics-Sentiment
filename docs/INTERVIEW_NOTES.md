# Interview-ready technical explanation

**Project:** CommerceLens — Automated E-commerce Analytics and Review Sentiment.

**Problem:** Listing prices, simulated demand measures, and sentiment samples are often difficult to compare without consistent data contracts, audit trails or reproducible SQL metrics.

**Workflow:** Generate sample data or import allowed CSV → validate numeric/date/review fields → record duplicates and rejected records → classify lexicon sentiment → persist SQLite snapshot → compute SQL window and group KPI queries → view Streamlit or offline HTML report.

**My implementation:** Python validation and transformations, SQLite schema and advanced SQL, reproducible fixture generator, local Streamlit visualizations, price-change/stock heuristics, 10 source-derived offline charts, and unit/integration CI.

**Technical choice:** A rule-based sentiment baseline is deterministic and explainable; no independent accuracy score can be asserted without a representative human-labeled dataset.

**Known limits:** Fictional prices and units, no audited order revenue, no live retailer API, no production authorization, no independently validated sentiment performance.

**Next work with a real sponsor:** Secure an official API and data processing permission, model multiple sellers, evaluate sentiment on an independent dataset, implement drift alerts and deploy behind authenticated HTTPS.
