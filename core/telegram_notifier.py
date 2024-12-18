import os

import requests

API_KEY = os.getenv("TELEGRAM_API_KEY")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

SEND_MESSAGE_API = f"https://api.telegram.org/bot{API_KEY}/sendMessage"

def send_message(text):
    data = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(SEND_MESSAGE_API, data=data)
    return response
