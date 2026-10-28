"""Transparent, synthetic-safe price change and latest-stock alerts."""
from math import isfinite
from src.analytics.metrics import rows

def build_alerts(conn, change_threshold=15.0, stock_threshold=10):
    if (not isinstance(change_threshold,(float,int)) or not isfinite(change_threshold)
       or change_threshold<=0 or type(stock_threshold) is not int or stock_threshold<0):
        raise ValueError("Alert thresholds must be a positive finite percentage and nonnegative integer stock")
    observations=rows(conn,"""WITH changed AS (
      SELECT product_id,product_name,observed_date,price,
             LAG(price) OVER(PARTITION BY product_id ORDER BY observed_date) previous_price
      FROM prices)
      SELECT product_id,product_name,observed_date,price,previous_price
      FROM changed WHERE previous_price>0 ORDER BY observed_date,product_id""")
    movements=[]
    for r in observations:
        delta=100*(r["price"]-r["previous_price"])/r["previous_price"]
        if abs(delta)>=change_threshold:
            movements.append({"product_id":r["product_id"],"date":r["observed_date"],
                "direction":"increase" if delta>0 else "decrease",
                "change_pct":round(delta,2),"old_price":r["previous_price"],
                "new_price":r["price"]})
    latest=rows(conn,"""WITH ranked AS (
      SELECT product_id,product_name,observed_date,inventory,
             ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY observed_date DESC) rn
      FROM prices)
      SELECT product_id,product_name,observed_date,inventory FROM ranked
      WHERE rn=1 AND inventory<=?""",(stock_threshold,))
    return {"change_threshold_pct":change_threshold,"stock_threshold_units":stock_threshold,
       "price_movements":movements,"low_stock":latest,
       "price_movement_count":len(movements),"low_stock_count":len(latest),
       "disclaimer":"Heuristic flags for observation review, not real-market alerts"}
