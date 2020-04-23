"""Django settings for production"""
import dj_database_url
from heimspiel.settings.base import *

DEBUG = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = [
    "heimspiel-backend.herokuapp.com",
]


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)

CORS_ORIGIN_ALLOW_ALL = True  # TODO: Remove as soon as frontend settings are done
