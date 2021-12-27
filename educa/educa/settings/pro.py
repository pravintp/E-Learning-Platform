from .base import *


DEBUG = False

ADMINS = (("pravin", "email@mydomain.com"),)

ALLOWED_HOSTS = [".educaproject.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "pravin77",
        "USER": "pravin77",
        "PASSWORD": "welcome",
        "HOST": "localhost",
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
