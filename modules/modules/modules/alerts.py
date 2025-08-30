import requests
from config import API_KEYS

def send_telegram_alert(message):
    token = API_KEYS["telegram_token"]
    chat_id = API_KEYS["telegram_chat_id"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print("Erreur Telegram :", response.text)
    except Exception as e:
        print("Échec de l'envoi Telegram :", e)
