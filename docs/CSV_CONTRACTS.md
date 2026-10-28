# CSV import contracts

## Input safety
- Only local file paths are accepted. Source licensing and privacy compliance are the operator's responsibility.
- Required price columns: product_id, product_name, category, seller, observed_date, price, list_price, inventory, units_sold.
- Required review columns: review_id, product_id, review_date, rating, review_text.
- Header duplicates and malformed over-wide rows fail before storing anything. Invalid value rows are rejected and counted in summary.json.
- Product IDs and observed_date form a unique logical observation key. The current implementation uses last-wins for duplicate product/day rows, regardless of seller; treat it as a documented source limitation.
- CSV export of comparisons prefixes leading Excel/Sheets formula operators in text values, reducing formula injection risks.

## Import example
~~~bash
python -m scripts.refresh --prices /approved/snapshot_prices.csv --reviews /approved/snapshot_reviews.csv
~~~

The source must be approved for processing before use. A workbook with formulas is not the same as a ready CSV dataset. Prices are assumed to use a consistent currency and numeric definitions; the system does not automatically convert currencies.

## Status
Demonstration uses deterministic fictional examples. No live retailer API authentication, third-party marketplace crawling, collection schedule or external reliability guarantee is built into this repository.
