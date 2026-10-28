"""Export ten SVG charts in one standalone local HTML report."""
import argparse,json
from src.analytics.report import render_report
def main():
    a=argparse.ArgumentParser()
    a.add_argument("--db",default="data/processed/commerce.sqlite")
    a.add_argument("--out",default="reports/commerce.html")
    p=a.parse_args()
    print(json.dumps(render_report(p.db,p.out),indent=2))
if __name__=="__main__":main()
