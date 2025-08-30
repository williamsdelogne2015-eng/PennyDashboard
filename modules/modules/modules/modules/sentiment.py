def analyze_sentiment(news_list):
    # Analyse simple : si des mots clés positifs sont présents, on considère la news comme positive
    keywords = ["contract", "approval", "partnership", "acquisition", "growth", "expansion", "FDA"]
    for news in news_list:
        if any(word.lower() in news.lower() for word in keywords):
            return "positif"
    return "neutre"
