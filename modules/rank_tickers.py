def rank_tickers(ticker_data_list):
    ranked = []
    for data in ticker_data_list:
        # Pondération des scores : tu peux ajuster les coefficients
        total = (
            data["Score News"] * 0.3 +
            data["Score Technique"] * 0.3 +
            data["Score Rebond"] * 0.4
        )
        ranked.append({
            "Ticker": data["ticker"],
            "Score News": data["Score News"],
            "Score Technique": data["Score Technique"],
            "Score Rebond": data["Score Rebond"],
            "Score Total": round(total, 2)
        })
    # Classement décroissant par score total
    return sorted(ranked, key=lambda x: x["Score Total"], reverse=True)
