import django_on_heroku
from decouple import config
import os
from .base import (
    STATIC_ROOT,
    STATIC_URL,
    MEDIA_URL,
    MEDIA_ROOT,
    DEBUG,
    SECRET_KEY,
    LANGUAGE_CODE,
    TIME_ZONE,
    USE_I18N,
    USE_TZ,
    INSTALLED_APPS,
    ROOT_URLCONF,
    AUTH_PASSWORD_VALIDATORS,
    MIDDLEWARE,
    TEMPLATES,
    DEFAULT_AUTO_FIELD,
    BASE_DIR
)

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

django_on_heroku.settings(locals())