from .common import *  # noqa: F403


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
        "HOST": "127.0.0.1",
        "USER": "root",
        "PASSWORD": "Az051277",
        "port": "3306",
    }
}
