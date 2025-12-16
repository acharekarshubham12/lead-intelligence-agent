# Lead Intelligence Agent – Live PubMed Integration

This project implements a production-ready **Lead Intelligence Agent**
focused on identifying, enriching, and ranking high-intent scientific
decision-makers using **live PubMed data**.

The system demonstrates how business development research can be automated
by combining:
- Scientific intent (recent publications)
- Role seniority
- Company context
- Deterministic propensity scoring

 No scraping of LinkedIn or private platforms is performed.
PubMed is accessed via its official public API.

---

## Key Features
- Live PubMed API integration (ESearch + EFetch)
- Extraction of recent authors in toxicology / 3D in-vitro research
- Deterministic 0–100 propensity scoring
- FastAPI backend
- Streamlit dashboard
- CSV export

---

## How to Run
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
streamlit run frontend/app.py
```

---

## Scoring Logic (Simplified)
- Recent PubMed publication (last 2 years): +40
- Senior role keyword (Director / Head): +30
- Funded / Biotech company (mocked): +20
- Hub location: +10

---

## Notes
- Company funding and roles are mocked for demo purposes
- PubMed data is live and real
- Designed for easy extension to LangChain / LLM agents