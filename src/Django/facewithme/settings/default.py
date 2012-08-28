# -*- coding: utf-8 -*-

PROJECT_ROOT = projectpath()
SECRET_KEY = 'b6vkv&le3%5#f**lwbzrzj@skw@t-)^evf&nv@1i%80bb)3h%n'

ROOT_URLCONF = 'settings.urls'
TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'pl'

DEBUG = False
TEMPLATE_DEBUG = False
ADMINS = (
    (u'Leszek Piątek', u'lpiatek@gmail.com')
)
MANAGERS = ()

USE_I18N = True
USE_L10N = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'apps.core',   
    'south',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


TEMPLATE_DIRS = ()

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

# APPS SETTINGS #########################################
# django.contrib.sites
SITE_ID = 1

# django.contrib.admin
ADMIN_MEDIA_PREFIX = '/static/admin/'

# django.contrib.staticfiles
STATIC_ROOT = projectpath('static')
STATIC_URL = '/static/'

# media files
MEDIA_ROOT = projectpath('media')
MEDIA_URL = '/media/'

# email
EMAIL_BACKEND = u'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = u'smtp.proste.pl'
EMAIL_HOST_PASSWORD = u'x8kv7fh4'
EMAIL_HOST_USER = u'fiesta-kawiarnia_kontakt'
EMAIL_USE_TLS = False
EMAIL_PORT = 587
EMAIL_SENDER = u'kontakt@fiesta-kawiarnia.pl'
EMAIL_DEFAULT_TO = [u'lpiatek@gmail.com', u'kontakt@fiesta-kawiarnia.pl']
EMAIL_TITLE_STRING = u'[fiesta-kawiarnia.pl] - %s'

# APPS SETTINGS #########################################
