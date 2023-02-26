# std
import requests
from decouple import config
import json

# 3rd
# local

TOKEN = config("TELEGRAM_BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/"
URL_S1_NOVA = "https://s1-nova.ru/app/private_test_python/"


def send_message(chat_id, text="stfu"):
    """
    Метод отправки сообщения клиенту методом sendMessage через API телеграмма
    Документация метода: https://core.telegram.org/bots/api#sendmessage
    """
    url = URL + "sendMessage"
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url=url, json=data)
    return response.json()


def send_user_data(data):
    """
    Метод отправки POST запроса данных о клиенте https://s1-nova.ru/app/private_test_python/
    """
    phone_number = data["message"]["text"]
    # login = data["message"]["login"]
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {"phone_number": phone_number, "login": "user667"}

    payload = json.dumps(body, indent=2)
    response = requests.post(url=URL_S1_NOVA, headers=headers, data=payload)
    # print(response.json())
    return True
