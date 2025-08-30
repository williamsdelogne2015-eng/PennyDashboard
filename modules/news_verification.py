import requests
from bs4 import BeautifulSoup

def get_api_news(ticker):
    # Simule une news récupérée via API
    return [{"headline": "FDA approval for TUYA"}]

def get_ir_news(url):
    # Scrape les titres de news depuis le site IR officiel
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    return [h.text.strip() for h in soup.find_all('h3')]

def cross_validate_news(api_news, ir_news):
    validated = []
    unconfirmed = []
    for n in api_news:
        if any(n["headline"].lower()[:50] in ir.lower() for ir in ir_news):
            validated.append(n)
        else:
            unconfirmed.append(n)
    return validated, unconfirmed
