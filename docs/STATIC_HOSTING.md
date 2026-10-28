# Source-derived static site and safe GitHub Pages setup

CommerceLens has a full Python/SQLite/Streamlit dashboard and a separate static report. The latter works without a server and includes ten real SQLite-derived SVG charts.

## Generate

~~~bash
python -m scripts.build_site --out public
~~~

Open public/index.html in a browser. The folder contains only index.html, metrics.json, robots.txt and .nojekyll. It never includes the raw sample CSVs, review text, or SQLite database.

GitHub Actions builds an artifact named commercelens-static-site automatically when source code changes. This downloadable artifact requires no hosting.

## GitHub Pages publication (manual)
1. Open this repository on GitHub.
2. Select Settings > Pages and set Build and deployment to GitHub Actions.
3. Open Actions > Publish CommerceLens static site on demand > Run workflow.
4. Only after that workflow succeeds, use the published URL shown in the deployment logs.

The manual trigger avoids repeatedly sending deployment requests while GitHub Pages may rate-limit the account. Static hosting does not run the Python backend, connect to a licensed retailer feed or provide authentication. A full Streamlit cloud service requires separate infrastructure.
