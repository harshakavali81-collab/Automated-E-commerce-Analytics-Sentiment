"""Build source-derived static website from fictional data; no dependencies or scraping."""
import argparse
import json
import shutil
from pathlib import Path
from src.pipeline.run import execute
from src.analytics.report import render_report

def build(out="public"):
    out=Path(out)
    if out.resolve()==Path(".").resolve():
        raise ValueError("Do not overwrite repository root")
    out.mkdir(parents=True,exist_ok=True)
    temp=out/"_fixture"
    info=execute(temp/"raw/prices.csv",temp/"raw/reviews.csv",temp/"processed",demo=True)
    report=render_report(temp/"processed/commerce.sqlite",out/"index.html",metadata=info)
    public={k:info[k] for k in ("source_kind","observation_count","product_count",
        "review_count","estimated_revenue","average_price","data_quality")}
    public["disclaimer"]="Fictional observations, simulated units, unvalidated sentiment"
    (out/"metrics.json").write_text(json.dumps(public,indent=2),encoding="utf-8")
    (out/".nojekyll").write_text("",encoding="utf-8")
    (out/"robots.txt").write_text("User-agent: *\nAllow: /\n",encoding="utf-8")
    shutil.rmtree(temp)
    return {"charts":report["charts"],"records":info["observation_count"],
        "files":sorted(p.name for p in out.iterdir() if p.is_file())}

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",default="public")
    args=parser.parse_args()
    print(json.dumps(build(args.out),indent=2))
