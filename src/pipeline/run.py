"""Reproducible CSV -> validation -> sentiment -> SQLite -> summary pipeline."""
import argparse,json,sqlite3
from pathlib import Path
from src.ingestion.generate_demo import generate
from src.ingestion.load_csv import read_csv
from src.processing.clean import clean_prices,clean_reviews
from src.sentiment.lexicon import label
from src.analytics.metrics import summary
from src.analytics.alerts import build_alerts
ROOT=Path(__file__).resolve().parents[2]
PRICE_COLUMNS=("product_id","product_name","category","seller","observed_date","price","list_price","inventory","units_sold")
REVIEW_COLUMNS=("review_id","product_id","review_date","rating","review_text")
def execute(prices=None,reviews=None,out=None,demo=False):
    prices=Path(prices) if prices else ROOT/"data/raw/prices.csv"
    reviews=Path(reviews) if reviews else ROOT/"data/raw/reviews.csv"
    out=Path(out) if out else ROOT/"data/processed"
    if demo:
        if prices.parent!=reviews.parent:raise ValueError("Demo paths need the same folder")
        generate(prices.parent)
    p,pq=clean_prices(read_csv(prices,required_columns=PRICE_COLUMNS))
    if not p:raise ValueError("All price observations were rejected")
    r,rq=clean_reviews(read_csv(reviews,required_columns=REVIEW_COLUMNS),{row[0] for row in p})
    out.mkdir(parents=True,exist_ok=True)
    with sqlite3.connect(out/"commerce.sqlite") as conn:
        conn.executescript((ROOT/"sql/schema.sql").read_text())
        conn.execute("DELETE FROM reviews")
        conn.execute("DELETE FROM prices")
        conn.executemany("INSERT INTO prices VALUES(?,?,?,?,?,?,?,?,?)",p)
        conn.executemany("INSERT INTO reviews VALUES(?,?,?,?,?,?)",[(*x,label(x[4])) for x in r])
        result=summary(conn)
        alerts=build_alerts(conn)
    (out/"alerts.json").write_text(json.dumps(alerts,indent=2),encoding="utf-8")
    result.update({"source_kind":"synthetic_demo" if demo else "user_supplied_csv_license_not_verified",
      "sentiment_method":"negation_aware_lexicon_not_benchmarked",
      "data_quality":{"prices":pq,"reviews":rq}})
    (out/"summary.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    return result
if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--demo",action="store_true")
    ap.add_argument("--prices",type=Path)
    ap.add_argument("--reviews",type=Path)
    ap.add_argument("--out",type=Path)
    args=ap.parse_args()
    if bool(args.prices)!=bool(args.reviews):ap.error("Both --prices and --reviews are required together")
    print(json.dumps(execute(args.prices,args.reviews,args.out,args.demo),indent=2))
