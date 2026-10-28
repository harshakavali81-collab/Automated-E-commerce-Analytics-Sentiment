# CommerceLens | Data Analyst / BI project

**Problem:** Compare SKU prices and customer-review sentiment while keeping data origin and KPI definitions auditable.

**Approach:** Designed a deterministic CSV-to-SQL pipeline with strict validation, transparent duplicate accounting, rule-based sentiment, category KPIs, advanced window-function SQL, interactive Streamlit filters, explainable price/stock flags and report exports.

**Tools:** Python, CSV, SQLite, Pandas, SQL, Streamlit, Plotly, Matplotlib, Docker, GitHub Actions.

**Evidence:** Python unit/integration test suite, automated dashboard and Docker checks, self-contained ten-chart report derived from the current database, ten presentation SVG figures. Latest CI run is linked from the Actions tab; do not claim a job passed unless it actually completed successfully.

**Scope disclosure:** The standard sample includes 12 fictional products tracked over 120 days (1,440 price observations). Units and review samples are invented, and estimated revenue is not transaction-level sales. The sentiment heuristic has not been validated against external annotation data.

**Interview focus:** Highlight integrity of data contracts, SQL reconciliation and reproducibility rather than false business outcomes. Be prepared to discuss multi-seller identity, source licensing, alert-threshold tuning and a real sentiment evaluation design.
