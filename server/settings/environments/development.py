"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

import socket

from server.settings.components.common import INSTALLED_APPS, MIDDLEWARE
from server.settings.components.database import DATABASES

# Setting the development status:

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',  # noqa: S104
    '127.0.0.1',
    '[::1]',
]

# https://django-debug-toolbar.readthedocs.io/en/stable/installation.html#configure-internal-ips
try:  # This might fail on some OS
    INTERNAL_IPS = [
        '{0}.1'.format(ip[:ip.rfind('.')])
        for ip in socket.gethostbyname_ex(socket.gethostname())[2]
    ]
except socket.error:  # pragma: no cover
    INTERNAL_IPS = []
INTERNAL_IPS += ['127.0.0.1', '10.0.2.2']


def _custom_show_toolbar(request) -> bool:
    """Only show the debug toolbar to users with the superuser flag."""
    return DEBUG and request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK':
        'server.settings.environments.development._custom_show_toolbar',
}

# Disable persistent DB connections
# https://docs.djangoproject.com/en/4.2/ref/databases/#caveats
DATABASES['default']['CONN_MAX_AGE'] = 0
