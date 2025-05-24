# utils.py
import requests
import os
from dotenv import load_dotenv

def send_telegram_message(chat_id: int, answer: str, userId: int, admin=False):
    load_dotenv()
    api_key = os.getenv("tg_token")
    token = api_key 
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": answer
    }
    response = requests.post(url, data=payload)
    return response
