def compute_scores(data):
    # Score basé sur la présence de news
    score_news = 25 if data["has_news"] else 0

    # Score technique basé sur le ratio de volume
    score_tech = 30 if data["volume_ratio"] >= 2 else 0

    # Score de rebond basé sur la chute récente
    score_rebond = 25 if data["chute_pct"] <= -25 else 0

    # Total des scores
    total = score_news + score_tech + score_rebond

    return {
        "Score News": score_news,
        "Score Technique": score_tech,
        "Score Rebond": score_rebond,
        "Score Total": total
    }
