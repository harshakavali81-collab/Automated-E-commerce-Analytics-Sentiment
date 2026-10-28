"""Offline self-contained HTML report, ten data-driven SVG charts; stdlib only."""
import json,sqlite3
from html import escape
from pathlib import Path
from src.analytics.metrics import summary,daily,categories,products,rows
from src.analytics.alerts import build_alerts

def line_chart(name,values):
    if not values:return "<p>No data for this chart.</p>"
    lo=min(values);hi=max(values);span=max(1e-9,hi-lo)
    coords=" ".join("%.1f,%.1f"%(50+620*i/max(len(values)-1,1),230-180*(v-lo)/span) for i,v in enumerate(values))
    return ('<svg viewBox="0 0 720 260" role="img" aria-label="'+escape(name,quote=True)+'">'
      '<title>'+escape(name)+'</title><line x1="50" y1="230" x2="680" y2="230" stroke="#608097"/>'
      '<polyline fill="none" stroke="#37dfb9" stroke-width="4" points="'+coords+'"/>'
      '<text x="12" y="26" fill="#bed3e3" font-size="13">'+str(round(hi,1))+'</text>'
      '<text x="12" y="230" fill="#bed3e3" font-size="13">'+str(round(lo,1))+'</text>'
      '</svg>')

def bar_chart(name,labels,values):
    if not values:return "<p>No data for this chart.</p>"
    scale=max(max(values),.001)
    out=['<svg viewBox="0 0 720 '+str(max(260,45*len(values)+35))+'" role="img" aria-label="'+escape(name,quote=True)+'">',
         '<title>'+escape(name)+'</title>']
    for i,(label,value) in enumerate(zip(labels,values)):
        y=25+45*i
        out.extend(['<text x="10" y="'+str(y+17)+'" fill="#eaf8ff" font-size="13">'+escape(str(label)[:24])+'</text>',
          '<rect x="220" y="'+str(y)+'" width="'+str(max(0,350*value/scale))+'" height="24" rx="4" fill="#46dfbc"/>',
          '<text x="587" y="'+str(y+17)+'" fill="#eaf8ff" font-size="13">'+str(round(value,1))+'</text>'])
    return "".join(out)+"</svg>"

def chart_series(conn):
    d=daily(conn);c=categories(conn);p=products(conn)
    s=rows(conn,"SELECT sentiment,COUNT(*) n FROM reviews GROUP BY sentiment ORDER BY sentiment")
    rating=rows(conn,"""SELECT p.category,AVG(r.rating) rating FROM reviews r
         JOIN (SELECT DISTINCT product_id,category FROM prices) p ON p.product_id=r.product_id
         GROUP BY p.category ORDER BY rating DESC""")
    v=rows(conn,"SELECT review_date,COUNT(*) n FROM reviews GROUP BY review_date ORDER BY review_date")
    return [
       ("Daily average price",line_chart("Daily average price",[x["avg_price"] for x in d])),
       ("Daily estimated revenue",line_chart("Daily estimated revenue",[x["estimated_revenue"] for x in d])),
       ("Estimated revenue by category",bar_chart("Estimated revenue by category",[x["category"] for x in c],[x["estimated_revenue"] for x in c])),
       ("Mean category price",bar_chart("Mean category price",[x["category"] for x in c],[x["avg_price"] for x in c])),
       ("Review sentiment labels",bar_chart("Review sentiment labels",[x["sentiment"] for x in s],[x["n"] for x in s])),
       ("Review rating by category",bar_chart("Review rating by category",[x["category"] for x in rating],[x["rating"] for x in rating])),
       ("Reference discounts (%)",bar_chart("Reference discounts",[x["category"] for x in c],[x["discount_pct"] for x in c])),
       ("Simulated product units",bar_chart("Simulated product units",[x["product_name"] for x in p[:10]],[x["units"] for x in p[:10]])),
       ("Review volume by day",line_chart("Review volume by day",[x["n"] for x in v])),
       ("Inventory by category",bar_chart("Inventory by category",[x["category"] for x in c],[x["stock"] for x in c]))]

def render_report(db="data/processed/commerce.sqlite",out="reports/commerce.html",metadata=None):
    with sqlite3.connect(db) as conn:
        metrics=summary(conn);figures=chart_series(conn);product_list=products(conn)
        alerts=build_alerts(conn)
    if metadata is None:
        src=Path(db).with_name("summary.json")
        metadata=json.loads(src.read_text(encoding="utf-8")) if src.exists() else {}
    safe=lambda s:escape(str(s),quote=True)
    panels="".join('<article class="panel chart"><p class="small">GRAPH %02d</p><h2>%s</h2>%s</article>'%(i+1,safe(title),svg) for i,(title,svg) in enumerate(figures))
    cards="".join('<div class="panel metric"><strong>%s</strong><span>%s</span></div>'%(safe(v),safe(k)) for k,v in [
        ("Product-day records",metrics["observation_count"]),
        ("Unique products",metrics["product_count"]),
        ("Estimated revenue (INR)","%.2f"%metrics["estimated_revenue"]),
        ("Sample reviews",metrics["review_count"])])
    table="".join("<tr>"+"".join("<td>"+safe(v)+"</td>" for v in (
        p["product_name"],p["category"],"%.2f"%p["avg_price"],p["units"],"%.2f"%p["estimated_revenue"]))+"</tr>"
        for p in product_list[:12])
    quality=safe(json.dumps(metadata.get("data_quality",{}),indent=2))
    source_kind=safe(metadata.get("source_kind","unverified"))
    html='''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>CommerceLens | Local snapshot analytics report</title>
<style>:root{color-scheme:dark;--bg:#0b1b2a;--panel:#142d40;--ink:#eaf9ff;--accent:#4adfc0}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 Arial,sans-serif}
main{max-width:1220px;padding:35px 18px;margin:auto}h1{font-size:clamp(32px,5vw,54px);line-height:1.12}
h2{font-size:20px;margin:5px 0 20px}.intro{color:#bed3df;max-width:850px}
.notice{padding:15px 20px;background:#3c3323;color:#ffe4b3;border:1px solid #a69061;border-radius:12px}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:20px}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:24px 0}
.panel{background:var(--panel);border-radius:15px;border:1px solid #33566b;padding:21px;min-width:0}
.metric strong{display:block;color:var(--accent);font-size:29px}.metric span,.small{color:#b0ccda;font-size:12px}
svg{width:100%;height:auto}table{border-collapse:collapse;width:100%}td,th{padding:9px;border-bottom:1px solid #365568;text-align:left}
th{color:var(--accent)}pre{white-space:pre-wrap;overflow-wrap:anywhere}
@media(max-width:900px){.grid{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,1fr)}}
</style></head><body><main><p class="small">COMMERCELENS | REPRODUCIBLE OFFLINE REPORT</p>
<h1>E-commerce trends &amp; sentiment</h1><p class="intro">Graphs below are computed from the current local SQLite snapshot.</p>
<div class="notice"><strong>Source: '''+source_kind+'''</strong>. Default data is synthetic. Price × simulated units
is NOT audited revenue. Sentiment is a rule-based, unvalidated baseline. This report never fetches live retailer data.</div>
<div class="stats">'''+cards+'''</div><div class="grid">'''+panels+'''</div>
<section class="panel" style="margin-top:20px"><h2>Product comparison</h2><div style="overflow:auto">
<table><thead><tr><th>Product</th><th>Category</th><th>Mean price</th><th>Units</th><th>Est. revenue</th></tr></thead><tbody>'''+table+'''</tbody></table></div></section>
<section class="panel" style="margin-top:20px"><h2>Quality and heuristic alert counts</h2><p>Price movements: '''+str(alerts["price_movement_count"])+'''. Latest low-stock records: '''+str(alerts["low_stock_count"])+'''.
These are observation heuristics only, not a real-time marketplace alert service.</p><pre>'''+quality+'''</pre></section>
<p class="small">Generated offline from source: <a href="https://github.com/harshakavali81-collab/Automated-E-commerce-Analytics-Sentiment">CommerceLens source on GitHub</a> &nbsp; | &nbsp; <a href="https://harshakavali81-collab.github.io/harshavardhan-portfolio/cases/commercelens.html">Full portfolio case study</a></p>
</main></body></html>'''
    path=Path(out);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(html,encoding="utf-8")
    return {"path":str(path),"charts":len(figures),"summary":metrics}
