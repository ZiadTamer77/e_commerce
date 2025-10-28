from .dev import *  # noqa: F403
import os

# Override DEBUG for tests
DEBUG = False

# Remove debug toolbar and silk from middleware for tests
MIDDLEWARE = [
    m
    for m in MIDDLEWARE  # noqa: F405
    if m
    not in [
        "silk.middleware.SilkyMiddleware",
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
]

# Remove debug toolbar and silk from installed apps for tests
INSTALLED_APPS = [
    app
    for app in INSTALLED_APPS  # noqa: F405
    if app
    not in [
        "silk",
        "debug_toolbar",
    ]
]


# Use a temporary directory for static files during tests
STATIC_ROOT = "/tmp/static"

# Create the directory if it doesn't exist
os.makedirs(STATIC_ROOT, exist_ok=True)
