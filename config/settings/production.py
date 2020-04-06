from .base import *

DEBUG = False
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'covid',
        'USER': 'admin',
        'PASSWORD': 'covid123.',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/Covid/covidBackEnd/static_root/'
APPSECRET_PROOF = False

# INSTALLED_APPS += ['debug_toolbar', ]
