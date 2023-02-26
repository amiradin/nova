from .base import *
from decouple import config

ALLOWED_HOSTS = ["98b7-37-99-39-112.eu.ngrok.io"]
# https://api.telegram.org/bot6069323888:AAGfimvGsrGFFyTQXZjE436qpQPqdpMb5KE/setWebhook?url=https://98b7-37-99-39-112.eu.ngrok.io/
# https://api.telegram.org/bot6069323888:AAGfimvGsrGFFyTQXZjE436qpQPqdpMb5KE/deleteWebhook?url=https://98b7-37-99-39-112.eu.ngrok.io/

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_NAME"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
    }
}
