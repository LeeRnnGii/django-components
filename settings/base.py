import os
import json
from pathlib import Path

##################
# PROJECT CONFIG #
##################
PROJECT_PACKAGE = Path(__file__).resolve().parent.parent
BASE_DIR = PROJECT_PACKAGE.parent
CONFIG_PATH = Path(os.environ.get('DJANGO_CONFIG_PATH',
                                  BASE_DIR.joinpath('config.json')))
##################
# CORE  SETTINGS #
##################
DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = False

ADMINS = []
INTERNAL_IPS = []
ALLOWED_HOSTS = []

USE_TZ = True
TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
LOCALE_PATHS = []

LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_COOKIE_AGE = None
LANGUAGE_COOKIE_DOMAIN = None
LANGUAGE_COOKIE_PATH = '/'
LANGUAGE_COOKIE_SECURE = False
LANGUAGE_COOKIE_HTTPONLY = False
LANGUAGE_COOKIE_SAMESITE = None

MANAGERS = ADMINS

DEFAULT_CHARSET = 'utf-8'

SERVER_EMAIL = 'root@localhost'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DATABASE_ROUTERS = []

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25

EMAIL_USE_LOCALTIME = False

EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None

DEFAULT_FROM_EMAIL = 'webmaster@localhost'

EMAIL_SUBJECT_PREFIX = '[Django] '

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

APPEND_SLASH = True

PREPEND_WWW = False

FORCE_SCRIPT_NAME = None

DISALLOWED_USER_AGENTS = []

ABSOLUTE_URL_OVERRIDES = {}

IGNORABLE_404_URLS = []

SECRET_KEY = ''

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

MEDIA_ROOT = BASE_DIR.joinpath('media')
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR.joinpath('static')
STATIC_URL = '/static/'

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000

FILE_UPLOAD_TEMP_DIR = None

FILE_UPLOAD_PERMISSIONS = 0o644

FILE_UPLOAD_DIRECTORY_PERMISSIONS = None

FORMAT_MODULE_PATH = None

DATE_FORMAT = 'N j, Y'

DATETIME_FORMAT = 'N j, Y, P'

TIME_FORMAT = 'P'

YEAR_MONTH_FORMAT = 'F Y'

MONTH_DAY_FORMAT = 'F j'

SHORT_DATE_FORMAT = 'm/d/Y'

SHORT_DATETIME_FORMAT = 'm/d/Y P'

DATE_INPUT_FORMATS = [
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y',  # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',             # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',             # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',             # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',             # '25 October 2006', '25 October, 2006'
]


TIME_INPUT_FORMATS = [
    '%H:%M:%S',     # '14:30:59'
    '%H:%M:%S.%f',  # '14:30:59.000200'
    '%H:%M',        # '14:30'
]


DATETIME_INPUT_FORMATS = [
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
]

FIRST_DAY_OF_WEEK = 0

DECIMAL_SEPARATOR = '.'

USE_THOUSAND_SEPARATOR = False

NUMBER_GROUPING = 0

THOUSAND_SEPARATOR = ','

DEFAULT_TABLESPACE = ''
DEFAULT_INDEX_TABLESPACE = ''

X_FRAME_OPTIONS = 'DENY'

USE_X_FORWARDED_HOST = False
USE_X_FORWARDED_PORT = False

WSGI_APPLICATION = 'Project.wsgi.application'

SECURE_PROXY_SSL_HEADER = None

DEFAULT_HASHING_ALGORITHM = 'sha256'

ROOT_URLCONF = 'Project.urls'
##############
# MIDDLEWARE #
##############
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
############
# SESSIONS #
############
# Cache to store session data if using the cache session backend.
SESSION_CACHE_ALIAS = 'default'
# Cookie name. This can be whatever you want.
SESSION_COOKIE_NAME = 'sessionid'
# Age of cookie, in seconds (default: 2 weeks).
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2
# A string like "example.com", or None for standard domain cookie.
SESSION_COOKIE_DOMAIN = None
# Whether the session cookie should be secure (https:// only).
SESSION_COOKIE_SECURE = False
# The path of the session cookie.
SESSION_COOKIE_PATH = '/'
# Whether to use the HttpOnly flag.
SESSION_COOKIE_HTTPONLY = True
# Whether to set the flag restricting cookie leaks on cross-site requests.
# This can be 'Lax', 'Strict', 'None', or False to disable the flag.
SESSION_COOKIE_SAMESITE = 'Lax'
# Whether to save the session data on every request.
SESSION_SAVE_EVERY_REQUEST = False
# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# The module to store session data
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# Directory to store session files if using the file session module. If None,
# the backend will use a sensible default.
SESSION_FILE_PATH = None
# class to serialize session data
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
#########
# CACHE #
#########
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_ALIAS = 'default'
##################
# AUTHENTICATION #
##################
AUTH_USER_MODEL = 'auth.User'

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = '/accounts/profile/'

LOGOUT_REDIRECT_URL = None

# # The number of days a password reset link is valid for
# PASSWORD_RESET_TIMEOUT_DAYS = 3

# # The number of seconds a password reset link is valid for (default: 3 days).
# PASSWORD_RESET_TIMEOUT = 60 * 60 * 24 * 3

# the first hasher in this list is the preferred algorithm.  any
# password using different algorithms will be converted automatically
# upon login
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
###########
# SIGNING #
###########
SIGNING_BACKEND = 'django.core.signing.TimestampSigner'
########
# CSRF #
########
# Dotted path to callable to be used as view when a request is
# rejected by the CSRF middleware.
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'

# Settings for CSRF cookie.
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_COOKIE_AGE = 60 * 60 * 24 * 7 * 52
CSRF_COOKIE_DOMAIN = None
CSRF_COOKIE_PATH = '/'
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'
CSRF_TRUSTED_ORIGINS = []
CSRF_USE_SESSIONS = False
############
# MESSAGES #
############
MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
###########
# LOGGING #
###########
# The callable to use to configure logging
LOGGING_CONFIG = 'logging.config.dictConfig'

# Custom logging configuration.
LOGGING = {}

# Default exception reporter class used in case none has been
# specifically assigned to the HttpRequest instance.
DEFAULT_EXCEPTION_REPORTER = 'django.views.debug.ExceptionReporter'

# Default exception reporter filter class used in case none has been
# specifically assigned to the HttpRequest instance.
DEFAULT_EXCEPTION_REPORTER_FILTER = 'django.views.debug.SafeExceptionReporterFilter'
###########
# TESTING #
###########
# The name of the class to use to run the test suite
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Apps that don't need to be serialized at test database creation time
# (only apps with migrations are to start with)
TEST_NON_SERIALIZED_APPS = []
############
# FIXTURES #
############
FIXTURE_DIRS = []
###############
# STATICFILES #
###############
# A list of locations of additional static files
STATICFILES_DIRS = []

# The default file storage backend used during the build process
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
]
##############
# MIGRATIONS #
##############
MIGRATION_MODULES = {}
#################
# SYSTEM CHECKS #
#################
SILENCED_SYSTEM_CHECKS = []
#######################
# SECURITY MIDDLEWARE #
#######################
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_SECONDS = 0
SECURE_REDIRECT_EXEMPT = []
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_SSL_HOST = None
SECURE_SSL_REDIRECT = False
