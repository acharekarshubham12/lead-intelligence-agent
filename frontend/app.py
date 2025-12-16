import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Lead Intelligence Dashboard", layout="wide")
st.title("🧬 Lead Intelligence Dashboard (Live PubMed)")

API_URL = "http://localhost:8000/leads"

with st.spinner("Fetching live PubMed data..."):
    data = requests.get(API_URL).json()

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

csv = df.to_csv(index=False).encode("utf-8")
st.download_button("⬇ Download CSV", csv, "ranked_pubmed_leads.csv", "text/csv")