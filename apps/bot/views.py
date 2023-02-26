# std
import json

# 3rd
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# local
from .services import send_message, send_user_data
from utils.validations import is_valid_phone_number
from utils.exceptions import ParseException

# https://api.telegram.org/bot6069323888:AAGfimvGsrGFFyTQXZjE436qpQPqdpMb5KE/sendMessage?chat_id=438894854&text=Hello!

keyboard = ReplyKeyboardMarkup(keyboard=[])


@csrf_exempt
def index(request):
    if request.method == "POST":
        body = request.body.decode("utf-8")
        data = json.loads(data)

        try:
            chat_id = data["message"]["chat"]["id"]
            message: str = data["message"]["text"]

            if message == "/start":
                send_message(chat_id=chat_id, text="Привет, а дай номер")
            elif is_valid_phone_number(message.strip()):
                response = send_user_data(data)
                if response:
                    send_message(chat_id=chat_id, text="Данные были отправлены!")
                else:
                    send_message(
                        chat_id=chat_id, text="Что-то пошло не так, попробуйте позже!"
                    )
                    HttpResponse({"success": False})
            else:
                send_message(chat_id=chat_id, text="Невалидный номер!")
        except Exception as e:
            raise e
    return HttpResponse({"success": True})
