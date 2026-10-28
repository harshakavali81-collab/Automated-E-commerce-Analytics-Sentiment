"""Validate, reject invalid data and report deduplication."""
from datetime import date
from math import isfinite
def convert_date(x):return date.fromisoformat(str(x).strip()).isoformat()
def number(x):
    n=float(x)
    if not isfinite(n):raise ValueError("Non-finite")
    return n
def clean_prices(rows):
    seen={};bad=0
    for r in rows:
        try:
            p=r["product_id"].strip();n=r["product_name"].strip()
            c=r["category"].strip();s=r["seller"].strip()
            day=convert_date(r["observed_date"])
            price=number(r["price"]);listed=number(r["list_price"])
            stock=int(r["inventory"]);units=int(r["units_sold"])
            if not all((p,n,c,s)) or min(price,listed)<=0 or min(stock,units)<0:raise ValueError()
            seen[(p,day)]=(p,n,c,s,day,price,listed,stock,units)
        except (ValueError,TypeError,KeyError,OverflowError):bad+=1
    result=sorted(seen.values(),key=lambda x:(x[4],x[0]))
    return result,{"raw":len(rows),"accepted":len(result),"rejected":bad,"duplicates":len(rows)-bad-len(result)}
def clean_reviews(rows,valid_product_ids):
    seen={};bad=0
    for r in rows:
        try:
            rid=r["review_id"].strip();pid=r["product_id"].strip()
            day=convert_date(r["review_date"]);rating=int(r["rating"]);text=r["review_text"].strip()[:3000]
            if not rid or pid not in valid_product_ids or not 1<=rating<=5 or not text:raise ValueError()
            seen[rid]=(rid,pid,day,rating,text)
        except (ValueError,TypeError,KeyError,OverflowError):bad+=1
    result=sorted(seen.values(),key=lambda x:x[0])
    return result,{"raw":len(rows),"accepted":len(result),"rejected":bad,"duplicates":len(rows)-bad-len(result)}
