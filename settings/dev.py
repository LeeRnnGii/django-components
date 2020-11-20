import os
import json
from .base import *

##################
# PROJECT CONFIG #
##################
try:
    with open(CONFIG_PATH) as config:
        CONFIG = json.load(config)
except IOError:
    print('DJANGO_CONFIG_PATH未配置或配置不正确')
    CONFIG = {
        'SECRET_KEY': '%0npj-xotd=of9t!8fy!86jl%cs#n$0&b^5tk%q$__c*l36+k0',
        'DEFAULT': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
##################
# CORE  SETTINGS #
##################
DEBUG = True
SECRET_KEY = CONFIG['SECRET_KEY']

TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-Hans'

INSTALLED_APPS.extend([])

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
DATABASE_ROUTERS = []
##############
# MIDDLEWARE #
##############

############
# SESSIONS #
############

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

#######################
# SECURITY MIDDLEWARE #
#######################

##################
# OTHER SETTINGS #
##################
# LOGIN_REDIRECT_URL = 'cars'
# LOGIN_URL = 'login'

# try:
#     import crispy_forms
# except ImportError:
#     print('未安装django-crispy-forms,可使用以下命令解决:pip install django-crispy-forms')
# else:
#     INSTALLED_APPS.append('crispy_forms')
#     CRISPY_FAIL_SILENTLY = not DEBUG
#     CRISPY_TEMPLATE_PACK = 'bootstrap4'

if DEBUG:
    try:
        import debug_toolbar
    except ImportError:
        print('未安装django-debug-toolbar,可使用以下命令解决:pip install django-debug-toolbar')
    else:
        INSTALLED_APPS.append('debug_toolbar')
        INTERNAL_IPS = ['127.0.0.1']
        MIDDLEWARE.insert(
            MIDDLEWARE.index('django.middleware.common.CommonMiddleware') + 1,
            'debug_toolbar.middleware.DebugToolbarMiddleware'
        )
