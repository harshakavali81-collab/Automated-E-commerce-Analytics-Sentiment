# Input data contracts

Prices CSV fields: product_id, product_name, category, seller, observed_date (YYYY-MM-DD), price (>0), list_price (>0), inventory (integer >=0), units_sold (integer >=0).

Reviews CSV fields: review_id, product_id (must match price product), review_date (YYYY-MM-DD), rating (1–5), review_text (nonempty). Derived sentiment: positive, neutral or negative.

Estimated revenue = sum(price * units_sold). This is NOT real merchant revenue. Average price is product-day weighted, not per transaction. Discount = (list_price-price)/list_price. Review sentiment share uses sample reviews as denominator and cannot represent all purchasers.
