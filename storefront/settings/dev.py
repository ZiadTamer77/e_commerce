from .common import *  # noqa: F403

import sys

if "tests" in sys.argv:
    DEBUG = False

DEBUG = True

SECRET_KEY = "django-insecure-gjwjbj(%35n9(xd9evo5e2*tx*d*p@2n$91th^vg&1qn!q4(b+"


if DEBUG:
    MIDDLEWARE += [  # noqa: F405
        "silk.middleware.SilkyMiddleware",
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "storefront3",
        "HOST": "mysql",
        "USER": "root",
        "PASSWORD": "Az051277",
        "port": "3306",
    }
}

# CELERY_BROKER_URL = "redis://redis:6379/1"

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://redis:6379/2",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         },
#     }
# }

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}
