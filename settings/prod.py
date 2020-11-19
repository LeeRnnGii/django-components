import os
from .common import *

try:
    with open(CONFIG_PATH) as config:
        CONFIG = json.load(config)
except IOError:
    raise IOError('DJANGO_CONFIG_PATH未配置或配置不正确')

##################
# CORE  SETTINGS #
##################
DEBUG = False

SECRET_KEY = CONFIG['SECRET_KEY']

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-Hans'

LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_COOKIE_AGE = None
LANGUAGE_COOKIE_DOMAIN = None
LANGUAGE_COOKIE_PATH = '/'
LANGUAGE_COOKIE_SECURE = False
LANGUAGE_COOKIE_HTTPONLY = False
LANGUAGE_COOKIE_SAMESITE = None

INSTALLED_APPS.extend(['users', 'cars'])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodb',
        'USER': CONFIG['DEFAULT']['USER'],
        'PASSWORD': CONFIG['DEFAULT']['PASSWORD'],
        'HOST': CONFIG['DEFAULT']['HOST'],
        'PORT': CONFIG['DEFAULT']['PORT'],
        'TEST': {
            'NAME': 'djangodbtest',
        },
    },

    'backup': {},
    'cache': {},
}
##############
# MIDDLEWARE #
##############

############
# SESSIONS #
############
SESSION_COOKIE_SECURE = True
#########
# CACHE #
#########

##################
# AUTHENTICATION #
##################

###########
# SIGNING #
###########

########
# CSRF #
########
CSRF_COOKIE_SECURE = True
############
# MESSAGES #
############

###########
# LOGGING #
###########

###########
# TESTING #
###########

############
# FIXTURES #
############

###############
# STATICFILES #
###############

##############
# MIGRATIONS #
##############

#################
# SYSTEM CHECKS #
#################

###########
# SSL/TLS #
###########
SECURE_HSTS_SECONDS = 60
SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

#######################
# SECURITY MIDDLEWARE #
#######################

##################
# OTHER SETTINGS #
##################
LOGIN_REDIRECT_URL = 'cars'
LOGIN_URL = 'login'