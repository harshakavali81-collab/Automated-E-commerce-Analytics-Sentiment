"""Rebuild SQLite and local HTML report using generated or authorized CSV data."""
import argparse,json
from pathlib import Path
from src.pipeline.run import execute
from src.analytics.report import render_report
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--demo",action="store_true")
    ap.add_argument("--prices",type=Path)
    ap.add_argument("--reviews",type=Path)
    ap.add_argument("--out",type=Path,default=Path("data/processed"))
    ap.add_argument("--report",type=Path,default=Path("reports/commerce.html"))
    a=ap.parse_args()
    if bool(a.prices)!=bool(a.reviews):ap.error("Supply --prices and --reviews together")
    if not a.demo and not a.prices:ap.error("Use --demo or provide authorized CSV files")
    m=execute(a.prices,a.reviews,a.out,a.demo)
    result=render_report(a.out/"commerce.sqlite",a.report,metadata=m)
    print(json.dumps({"source":m["source_kind"],"observations":m["observation_count"],"charts":result["charts"],"report":result["path"]},indent=2))
if __name__=="__main__":main()
