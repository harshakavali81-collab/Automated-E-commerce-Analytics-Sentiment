"""Export 10 source-driven matplotlib figures from the current SQLite database."""
import argparse,sqlite3
from pathlib import Path
from src.analytics.metrics import daily,categories,products,rows
def render(db="data/processed/commerce.sqlite",out="docs/generated-charts"):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    dest=Path(out);dest.mkdir(parents=True,exist_ok=True)
    with sqlite3.connect(db) as con:
        d=daily(con);c=categories(con);p=products(con)
        s=rows(con,"SELECT sentiment, COUNT(*) n FROM reviews GROUP BY sentiment")
        r=rows(con,"SELECT review_date, COUNT(*) n FROM reviews GROUP BY review_date ORDER BY review_date")
        ratings=rows(con,"SELECT p.category, ROUND(AVG(r.rating),2) rating FROM reviews r JOIN (SELECT DISTINCT product_id,category FROM prices) p ON r.product_id=p.product_id GROUP BY p.category")
    jobs=[("01-price",d,"observed_date","avg_price","Daily average price","line"),
      ("02-revenue",d,"observed_date","estimated_revenue","Estimated daily revenue","line"),
      ("03-category-revenue",c,"category","estimated_revenue","Estimated revenue by category","bar"),
      ("04-category-price",c,"category","avg_price","Average price by category","bar"),
      ("05-sentiment",s,"sentiment","n","Review sentiment mix","bar"),
      ("06-ratings",ratings,"category","rating","Average rating by category","bar"),
      ("07-discount",c,"category","discount_pct","Average list-price discount","bar"),
      ("08-products",p[:10],"product_name","units","Simulated units by product","bar"),
      ("09-review-volume",r,"review_date","n","Review volume","line"),
      ("10-inventory",c,"category","stock","Reported inventory proxy","bar")]
    paths=[]
    for slug,records,x,y,title,kind in jobs:
        labels=[str(z[x]) for z in records];values=[z[y] for z in records]
        fig,ax=plt.subplots(figsize=(10,5))
        if kind=="line":
            ax.plot(range(len(labels)),values,linewidth=2);ax.set_xlabel("Chronological row index")
        else:
            ax.bar(range(len(labels)),values);ax.set_xticks(range(len(labels)),labels,rotation=25,ha="right")
        ax.set_title(title)
        fig.text(0.13,0.01,"Synthetic default: no independently measured real retailer data",fontsize=9)
        fig.tight_layout(rect=(0,0.04,1,1))
        target=dest/(slug+".png");fig.savefig(target,dpi=140);plt.close(fig);paths.append(str(target))
    return paths
if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("--db",default="data/processed/commerce.sqlite")
    a.add_argument("--out",default="docs/generated-charts")
    args=a.parse_args()
    print("\n".join(render(args.db,args.out)))
