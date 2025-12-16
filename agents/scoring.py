def score_lead(lead):
    score = 0

    if lead.get("recent_publication"):
        score += 40

    title = lead.get("title", "").lower()
    if "director" in title or "head" in title:
        score += 30

    if lead.get("company_funded"):
        score += 20

    if lead.get("hub_location"):
        score += 10

    return min(score, 100)