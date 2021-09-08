"""
Base settings to build other settings files upon.
"""
from pathlib import Path

import environ

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

# LOCALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = env.str(var="TIME_ZONE", default="UTC")
USE_I18N = True
USE_L10N = True
USE_TZ = env.bool(var="USE_TZ", default=True)
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# DATABASES
DATABASES = {"default": env.db("DATABASE_URL")}
# DATABASES["default"]["ATOMIC_REQUESTS"] = True

# URLS
ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"

# APPS
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPS = [
    "rest_framework",
]

LOCAL_APPS = [
    "fleet",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# STATIC
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATIC_URL = "/static/"

# MEDIA
MEDIA_ROOT = str(ROOT_DIR / "media")
MEDIA_URL = "/media/"

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# SECURITY
# SESSION_COOKIE_HTTPONLY = True
# CSRF_COOKIE_HTTPONLY = True
# SECURE_BROWSER_XSS_FILTER = True
# X_FRAME_OPTIONS = "DENY"
# SESSION_COOKIE_SECURE = False
# SECURE_CONTENT_TYPE_NOSNIFF = True
# CSRF_COOKIE_SECURE = False

# ADMIN
ADMIN_URL = env.str(var="ADMIN_URL", default="admin/")
# LOGGING
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "%(levelname)s %(asctime)s %(module)s "
#             "%(process)d %(thread)d %(message)s"
#         }
#     },
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "verbose",
#         }
#     },
#     "root": {"level": "INFO", "handlers": ["console"]},
# }
