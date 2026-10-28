-- All money/units are fictional estimates by default, not real orders.

-- A. Historical product price changes using chronological window functions.
WITH history AS (
 SELECT product_id,product_name,observed_date,price,
 LAG(price) OVER(PARTITION BY product_id ORDER BY observed_date) prev_price
 FROM prices
)
SELECT product_id,product_name,observed_date,
 ROUND(100.0*(price-prev_price)/prev_price,2) change_pct
FROM history WHERE prev_price>0 ORDER BY ABS(change_pct) DESC LIMIT 20;

-- B. Category rank of simulated estimated revenue.
WITH item AS (
 SELECT product_id,MAX(product_name) product_name,MAX(category) category,
 SUM(price*units_sold) estimated_revenue FROM prices GROUP BY product_id
)
SELECT category,product_name,ROUND(estimated_revenue,2) estimated_revenue,
 DENSE_RANK() OVER(PARTITION BY category ORDER BY estimated_revenue DESC) category_rank
FROM item ORDER BY category,category_rank;

-- C. Seven-day moving average of category-listed prices.
WITH daily AS (
 SELECT observed_date,category,AVG(price) avg_price
 FROM prices GROUP BY observed_date,category
)
SELECT observed_date,category,ROUND(avg_price,2) avg_price,
 ROUND(AVG(avg_price) OVER(PARTITION BY category ORDER BY observed_date
 ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) mean_price_7d
FROM daily ORDER BY category,observed_date;

-- D. Latest observed stock per product.
WITH ranked AS (
 SELECT product_id,product_name,category,observed_date,inventory,
 ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY observed_date DESC) rn
 FROM prices
)
SELECT product_id,product_name,category,observed_date,inventory
FROM ranked WHERE rn=1 ORDER BY inventory;

-- E. Review rating by category without duplicate fanout.
SELECT p.category,COUNT(*) sampled_reviews,ROUND(AVG(r.rating),2) mean_rating
FROM reviews r JOIN (SELECT DISTINCT product_id,category FROM prices) p
ON p.product_id=r.product_id GROUP BY p.category ORDER BY sampled_reviews DESC;
