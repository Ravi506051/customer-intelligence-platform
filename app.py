import streamlit as st, pandas as pd, numpy as np, plotly.express as px
st.set_page_config(layout="wide"); st.title("Customer Intelligence Platform")
st.caption("Synthetic demo data; upload a customer CSV to explore real data.")
up=st.file_uploader("Customer CSV",type="csv")
if up: d=pd.read_csv(up)
else:
 r=np.random.default_rng(42); n=1200
 d=pd.DataFrame({"customer_id":[f"C{i:04}" for i in range(n)],"orders":r.poisson(4,n)+1,"spend":r.gamma(2.2,85,n),"recency_days":r.integers(1,365,n),"region":r.choice(["North","South","East","West"],n)})
d["avg_order_value"]=d.spend/d.orders
d["segment"]=pd.qcut(d.spend.rank(method="first"),4,labels=["Bronze","Silver","Gold","Platinum"])
a,b,c=st.columns(3); a.metric("Customers",len(d)); b.metric("Revenue",f"${d.spend.sum():,.0f}"); c.metric("At risk",int((d.recency_days>180).sum()))
st.plotly_chart(px.box(d,x="segment",y="spend",color="segment"),use_container_width=True)
st.plotly_chart(px.histogram(d,x="recency_days",color="region"),use_container_width=True)
st.dataframe(d.sort_values("spend",ascending=False).head(50),use_container_width=True)
st.download_button("Export CSV",d.to_csv(index=False),"customer_insights.csv")
