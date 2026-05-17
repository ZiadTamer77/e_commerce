import os
import dj_database_url
from .common import *  # noqa: F403

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["app.ziadco.com", "localhost", "127.0.0.1", "*"]

INSTALLED_APPS = [app for app in INSTALLED_APPS if app not in ["debug_toolbar", "silk"]]

CSRF_TRUSTED_ORIGINS = ["https://app.ziadco.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

# REDIS_URL = os.environ["REDISCLOUD_URL"]

# CELERY_BROKER_URL = REDIS_URL


# CACHES = {
#    "default": {
#        "BACKEND": "django_redis.cache.RedisCache",
#        "LOCATION": REDIS_URL,
#        "OPTIONS": {
#            "CLIENT_CLASS": "django_redis.client.DefaultClient",
#        },
#    }
# }
