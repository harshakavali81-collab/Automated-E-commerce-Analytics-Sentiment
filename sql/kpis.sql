-- Revenue is only a price x fictional units estimate, NOT audited transactions.
SELECT category,ROUND(AVG(price),2) AS avg_price,
 ROUND(SUM(price*units_sold),2) AS estimated_revenue,
 SUM(units_sold) AS units,COUNT(*) AS product_days
FROM prices GROUP BY category ORDER BY estimated_revenue DESC;

SELECT observed_date,ROUND(AVG(price),2) AS avg_price,
 ROUND(SUM(price*units_sold),2) AS estimated_revenue
FROM prices GROUP BY observed_date ORDER BY observed_date;

SELECT sentiment,COUNT(*) AS reviews,
 ROUND(100.0*COUNT(*)/(SELECT COUNT(*) FROM reviews),2) AS sentiment_pct
FROM reviews GROUP BY sentiment ORDER BY reviews DESC;

WITH ranked AS(
 SELECT product_id,product_name,observed_date,price,
 ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY observed_date) AS first_row,
 ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY observed_date DESC) AS last_row
 FROM prices)
SELECT a.product_name,a.price AS first_price,b.price AS last_price,
 ROUND(100.0*(b.price-a.price)/a.price,2) AS price_change_pct
FROM ranked a JOIN ranked b ON a.product_id=b.product_id
WHERE a.first_row=1 AND b.last_row=1 ORDER BY price_change_pct DESC;
