def get_valid_tickers(market):
    # Simulation simple de tickers selon le marché
    return [
        {
            "ticker": "TUYA",
            "volume_ratio": 2.5,
            "chute_pct": -30,
            "structure_clean": True,
            "sentiment": "positif",
            "has_news": True,
            "ir_url": "https://ir.tuya.com/news-releases"
        },
        {
            "ticker": "IMPP",
            "volume_ratio": 1.8,
            "chute_pct": -20,
            "structure_clean": True,
            "sentiment": "neutre",
            "has_news": False,
            "ir_url": "https://www.imperialpetroleuminc.com/investor-relations"
        }
    ]
