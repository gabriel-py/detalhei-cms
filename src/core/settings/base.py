from datetime import timedelta
from pathlib import Path
# from decouple import config
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# DEBUG = config("DEBUG", cast=bool)
# SECRET_KEY = config('SECRET_KEY')
DEBUG = True
SECRET_KEY = 'pihu_d^_!8r$6n7^_bozy_b^4d5s-@hnuoqqd4+rb%9vvy9)m9'
SITE_ID = 1

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


INSTALLED_APPS = [
    'django_stisla',
    "django.contrib.admin",
    "django.contrib.auth",
    'widget_tweaks',
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    # 'django.contrib.sites',

    # LIBS
    # 'nested_admin',
    # 'rest_framework',
    # 'rest_framework.authtoken',
    # 'drf_yasg',
    # 'core',
    'access',
    'produto',
    'detalhei',
    'blog'
]

ROOT_URLCONF = "core.urls"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.request',
            ],
        },
    },
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)

ALLOWED_HOSTS = []

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'BLACKLIST_AFTER_ROTATION': False,
    'SIGNING_KEY': SECRET_KEY,
}

WSGI_APPLICATION = "core.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"