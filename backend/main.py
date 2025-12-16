from fastapi import FastAPI
from agents.pubmed_agent import fetch_recent_authors
from agents.scoring import score_lead

app = FastAPI(title="Lead Intelligence API – PubMed Live")

@app.get("/leads")
def get_leads():
    authors = fetch_recent_authors(
        query="drug induced liver injury OR 3D in vitro models",
        max_results=10
    )

    leads = []
    for name in authors:
        lead = {
            "name": name,
            "title": "Director of Toxicology",  # mocked
            "company": "Biotech Co",            # mocked
            "recent_publication": True,
            "company_funded": True,
            "hub_location": True
        }
        lead["score"] = score_lead(lead)
        leads.append(lead)

    return sorted(leads, key=lambda x: x["score"], reverse=True)