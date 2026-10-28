"""Deterministic fictional e-commerce dataset. No scraping."""
import csv, random
from pathlib import Path
from datetime import date,timedelta
ITEMS=[("P01","Wireless Mouse","Electronics",899),("P02","USB Hub","Electronics",1799),
("P03","Bluetooth Speaker","Electronics",2499),("P04","Cotton T-shirt","Fashion",649),
("P05","Sneakers","Fashion",2199),("P06","Backpack","Fashion",1599),
("P07","Ceramic Mugs","Home",899),("P08","Desk Lamp","Home",1299),
("P09","Storage Baskets","Home",1099),("P10","Yoga Mat","Fitness",1199),
("P11","Water Bottle","Fitness",799),("P12","Resistance Bands","Fitness",999)]
TEXT=[(5,"Excellent quality, fast delivery, love it"),(4,"Good and useful product"),
(3,"Average product, okay value"),(2,"Poor quality, slow shipping"),
(1,"Terrible, broken and bad"),(4,"Not bad, great value"),
(2,"Not good, disappointing"),(5,"Amazing, reliable and comfortable")]
def write(path,rows,cols):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",newline="",encoding="utf-8") as fp:
        w=csv.DictWriter(fp,fieldnames=cols);w.writeheader();w.writerows(rows)
def generate(folder="data/raw",days=120,seed=42):
    rng=random.Random(seed);prices=[];reviews=[]
    for i in range(days):
        day=(date(2026,1,1)+timedelta(days=i)).isoformat()
        for k,(pid,name,cat,base) in enumerate(ITEMS):
            price=round(base*(1+0.001*i+0.02*((i//7)%5-2))*(1+rng.uniform(-0.07,0.07)),2)
            units=max(0,round(19+rng.gauss(0,7)+k%5))
            prices.append(dict(product_id=pid,product_name=name,category=cat,seller="Demo Merchant "+str(k%3+1),
              observed_date=day,price=price,list_price=round(base*1.22,2),inventory=max(0,100-units),units_sold=units))
            if i%9==k%9:
                rating,review=TEXT[(i//9+k+rng.randrange(2))%len(TEXT)]
                reviews.append(dict(review_id="R"+str(len(reviews)+1).zfill(5),product_id=pid,
                    review_date=day,rating=rating,review_text=review))
    folder=Path(folder)
    write(folder/"prices.csv",prices,["product_id","product_name","category","seller","observed_date","price","list_price","inventory","units_sold"])
    write(folder/"reviews.csv",reviews,["review_id","product_id","review_date","rating","review_text"])
    return len(prices),len(reviews)
if __name__=="__main__":print(generate())
