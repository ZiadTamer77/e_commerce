import os
import dj_database_url
from .common import *  # noqa: F403

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["zbuy-b8ec4d6bf62a.herokuapp.com"]

DATABASES = {"default": dj_database_url.config()}

REDIS_URL = os.environ["REDISCLOUD_URL"]

CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
