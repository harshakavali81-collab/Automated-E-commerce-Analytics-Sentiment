"""Streamlit product-pricing and customer sentiment explorer."""
import json,sqlite3
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st
root=Path(__file__).resolve().parents[1]
db=root/"data/processed/commerce.sqlite"
meta=root/"data/processed/summary.json"
st.set_page_config(page_title="CommerceLens BI",page_icon="🛒",layout="wide")
st.title("🛒 CommerceLens — E-commerce Analytics & Sentiment")
st.caption("Portfolio demonstration, not a verified retail data feed")
if not db.exists() or not meta.exists():
    st.info("Run python -m src.pipeline.run --demo first.")
    st.stop()
provenance=json.loads(meta.read_text())
st.warning("Source: "+provenance["source_kind"]+" | Revenue is simulated price × units, NOT audited transactions | Review sentiment is an unvalidated rule-based baseline.")
with sqlite3.connect(db) as con:
    prices=pd.read_sql_query("SELECT * FROM prices",con)
    reviews=pd.read_sql_query("SELECT r.*,p.category FROM reviews r JOIN (SELECT DISTINCT product_id,category FROM prices) p ON p.product_id=r.product_id",con)
selection=st.sidebar.multiselect("Select categories",sorted(prices.category.unique()),default=sorted(prices.category.unique()))
if not selection:st.info("Select at least one category");st.stop()
prices=prices[prices.category.isin(selection)].copy()
reviews=reviews[reviews.category.isin(selection)]
start,end=prices.observed_date.min(),prices.observed_date.max()
from datetime import date
first_day,last_day=date.fromisoformat(start),date.fromisoformat(end)
period=st.sidebar.date_input("Observation date",value=(first_day,last_day),min_value=first_day,max_value=last_day)
if len(period)!=2:
    st.info("Choose both start and end dates.")
    st.stop()
low,high=(d.isoformat() for d in period)
prices=prices[prices.observed_date.between(low,high)].copy()
reviews=reviews[reviews.review_date.between(low,high)].copy()
if prices.empty:st.info("No observations for this selection");st.stop()
prices["estimated_revenue"]=prices.price*prices.units_sold
prices["discount_pct"]=(prices.list_price-prices.price)/prices.list_price*100
cols=st.columns(4)
cols[0].metric("Product-day records",f"{len(prices):,}")
cols[1].metric("Products",prices.product_id.nunique())
cols[2].metric("Estimated revenue",f"₹{prices.estimated_revenue.sum():,.0f}")
cols[3].metric("Reviews",len(reviews))
daily=prices.groupby("observed_date",as_index=False).agg(avg_price=("price","mean"),estimated_revenue=("estimated_revenue","sum"))
cats=prices.groupby("category",as_index=False).agg(estimated_revenue=("estimated_revenue","sum"),discount=("discount_pct","mean"),stock=("inventory","mean"))
a,b=st.columns(2)
with a:
    st.plotly_chart(px.line(daily,x="observed_date",y="avg_price",title="Average observed price"),use_container_width=True)
    st.plotly_chart(px.bar(cats,x="category",y="estimated_revenue",title="Category estimated revenue"),use_container_width=True)
    st.plotly_chart(px.bar(cats,x="category",y="discount",title="Average reference discount %"),use_container_width=True)
with b:
    st.plotly_chart(px.line(daily,x="observed_date",y="estimated_revenue",title="Daily estimated revenue"),use_container_width=True)
    st.plotly_chart(px.bar(cats,x="category",y="stock",title="Inventory proxy"),use_container_width=True)
    if len(reviews):
        sentiment=reviews.groupby("sentiment",as_index=False).size()
        st.plotly_chart(px.pie(sentiment,names="sentiment",values="size",title="Rule-based review labels"),use_container_width=True)
        rating=reviews.groupby("category",as_index=False).rating.mean()
        st.plotly_chart(px.bar(rating,x="category",y="rating",title="Review rating by category"),use_container_width=True)
    else:st.info("No reviews in selected date range.")
st.subheader("Product price comparison")
detail=prices.groupby(["product_id","product_name","category"],as_index=False).agg(
 minimum=("price","min"),average=("price","mean"),maximum=("price","max"),
 estimated_revenue=("estimated_revenue","sum"))
st.dataframe(detail,use_container_width=True,hide_index=True)
st.download_button("Download filtered CSV",detail.to_csv(index=False).encode(),file_name="comparison.csv",mime="text/csv")
with st.expander("Data provenance and quality checks"):
    st.json(provenance)
