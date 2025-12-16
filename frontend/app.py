import streamlit as st
import pandas as pd

from agents.pubmed_agent import fetch_recent_authors
from agents.scoring import score_lead

# Page settings
st.set_page_config(
    page_title="Lead Intelligence Agent",
    layout="wide"
)

# Title
st.title("Lead Intelligence Agent")
st.write(
    "This application identifies and ranks scientific leads using live PubMed data."
)

# Fetch data from PubMed
st.write("Fetching recent authors from PubMed...")
authors = fetch_recent_authors(
    query="drug induced liver injury OR 3D in vitro models",
    max_results=15
)

# Create lead list
leads = []

for author in authors:
    lead = {}
    lead["Name"] = author
    lead["Title"] = "Director of Toxicology"   # mock data for demo
    lead["Company"] = "Biotech Company"        # mock data for demo
    lead["Source"] = "PubMed"

    # Calculate lead score
    lead["Score"] = score_lead({
        "recent_publication": True,
        "title": lead["Title"],
        "company_funded": True,
        "hub_location": True
    })

    leads.append(lead)

# Convert to DataFrame
df = pd.DataFrame(leads)

# Sort by score
df = df.sort_values("Score", ascending=False)

# Show table
st.subheader("Ranked Leads")
st.dataframe(df, use_container_width=True)

# Download CSV
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="ranked_pubmed_leads.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: grey;'>Powered by Shubham</div>",
    unsafe_allow_html=True
)
