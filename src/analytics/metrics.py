"""SQL aggregations over a validated snapshot."""
def rows(conn,query):
    cursor=conn.execute(query)
    cols=[x[0] for x in cursor.description]
    return [dict(zip(cols,r)) for r in cursor.fetchall()]
def summary(conn):
    one=lambda q:conn.execute(q).fetchone()[0]
    return {
      "observation_count":one("SELECT COUNT(*) FROM prices"),
      "product_count":one("SELECT COUNT(DISTINCT product_id) FROM prices"),
      "review_count":one("SELECT COUNT(*) FROM reviews"),
      "estimated_revenue":round(one("SELECT COALESCE(SUM(price*units_sold),0) FROM prices"),2),
      "average_price":round(one("SELECT COALESCE(AVG(price),0) FROM prices"),2),
      "average_rating":round(one("SELECT COALESCE(AVG(rating),0) FROM reviews"),2),
      "start_date":one("SELECT MIN(observed_date) FROM prices"),
      "end_date":one("SELECT MAX(observed_date) FROM prices"),
      "sentiment_counts":{r["sentiment"]:r["n"] for r in rows(conn,"SELECT sentiment,COUNT(*) n FROM reviews GROUP BY sentiment")},
      "revenue_disclaimer":"Price x generated units only; NOT real sales revenue"}
def daily(conn):
    return rows(conn,"SELECT observed_date,ROUND(AVG(price),2) avg_price,ROUND(SUM(price*units_sold),2) estimated_revenue, SUM(units_sold) units FROM prices GROUP BY observed_date ORDER BY observed_date")
def categories(conn):
    return rows(conn,"SELECT category,ROUND(AVG(price),2) avg_price,ROUND(AVG((list_price-price)*100/list_price),2) discount_pct,ROUND(SUM(price*units_sold),2) estimated_revenue,SUM(units_sold) units,ROUND(AVG(inventory),2) stock FROM prices GROUP BY category ORDER BY estimated_revenue DESC")
def products(conn):
    return rows(conn,"SELECT product_id,MAX(product_name) product_name,MAX(category) category,ROUND(AVG(price),2) avg_price,ROUND(MIN(price),2) min_price,ROUND(MAX(price),2) max_price,ROUND(SUM(price*units_sold),2) estimated_revenue,SUM(units_sold) units FROM prices GROUP BY product_id ORDER BY estimated_revenue DESC")
