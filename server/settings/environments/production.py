"""
This file contains all the settings used in production.

This file is required and if development.py is present these
values are overridden.
"""

from server.settings.components import config
from server.settings.components.common import MIDDLEWARE


# Production flags:
# https://docs.djangoproject.com/en/4.2/howto/deployment/

DEBUG = False

ALLOWED_HOSTS = config('DOMAINS').split(' ')

MIDDLEWARE += (
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

# Staticfiles
# https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/

# This is a hack to allow a special flag to be used with `--dry-run`
# to test things locally.
_COLLECTSTATIC_DRYRUN = config(
    'DJANGO_COLLECTSTATIC_DRYRUN', cast=bool, default=False,
)
# Adding STATIC_ROOT to collect static files via 'collectstatic':
STATIC_ROOT = '.static' if _COLLECTSTATIC_DRYRUN else '/var/www/django/static'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

# Media files
# https://docs.djangoproject.com/en/4.2/topics/files/

MEDIA_ROOT = '/var/www/django/media'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

_PASS = 'django.contrib.auth.password_validation'  # noqa: S105
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': '{0}.UserAttributeSimilarityValidator'.format(_PASS)},
    {'NAME': '{0}.MinimumLengthValidator'.format(_PASS)},
    {'NAME': '{0}.CommonPasswordValidator'.format(_PASS)},
    {'NAME': '{0}.NumericPasswordValidator'.format(_PASS)},
]


# Security
# https://docs.djangoproject.com/en/4.2/topics/security/

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
