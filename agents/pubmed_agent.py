import requests
import xml.etree.ElementTree as ET

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def fetch_recent_authors(
    query="drug induced liver injury",
    max_results=20
):
    # 1. Search PubMed
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }

    search_resp = requests.get(PUBMED_SEARCH_URL, params=search_params)
    search_resp.raise_for_status()

    ids = search_resp.json().get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []

    # 2. Fetch article details
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }

    fetch_resp = requests.get(PUBMED_FETCH_URL, params=fetch_params)
    fetch_resp.raise_for_status()

    root = ET.fromstring(fetch_resp.text)

    authors = set()

    # 3. Robust author extraction
    for author in root.findall(".//Author"):
        last = author.findtext("LastName")
        fore = author.findtext("ForeName")
        collective = author.findtext("CollectiveName")

        if collective:
            authors.add(collective)
        elif last and fore:
            authors.add(f"{fore} {last}")
        elif last:
            authors.add(last)

    return list(authors)
