import socket

from .base import *  # noqa
from .base import env

# GENERAL
DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="ezRuZHIzeV9wMWRyfQ==",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


# django-debug-toolbar
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
# set internal ips in docker

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
