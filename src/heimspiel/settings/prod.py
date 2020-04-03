"""Django settings for production"""

DEBUG = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = [
    "heimspiel.pythonanywhere.com",
]

STATIC_ROOT = "/home/heimspiel/heimspiel-backend/src/static/"
MEDIA_ROOT = "/home/heimspiel/heimspiel-backend/src/media/"

CORS_ORIGIN_ALLOW_ALL = True  # TODO: Remove as soon as frontend settings are done
