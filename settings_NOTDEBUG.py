"""
Django settings for djangotest project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from . import secrets_env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'i889r8a3_s0coueb=fyt_c3aulr5tb$&o#u!f7o9t8yqr3plj^'
# from django.core.management.utils import get_random_secret_key
# get_random_secret_key()
SECRET_KEY = secrets_env.key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = ['*', u'127.0.0.1', u'localhost']
ALLOWED_HOSTS = [secrets_env.allowed_host, u'127.0.0.1', u'localhost']

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options:
# 1. ALLOW-FROM is an obsolete directive that no longer works in modern browsers. Don't use it.
# 2. Does not seem to change headers anyway
# X_FRAME_OPTIONS = 'ALLOW-FROM https://sok.folke.isof.se'

# https://www.geeksforgeeks.org/adding-csp-headers-in-django-project/

# uri to report policy violations CSP_REPORT_URI = '<add your reporting uri>'

# default source as self
CSP_DEFAULT_SRC = ("'self'",)

# images from our domain and other domains
CSP_IMG_SRC = ("'self'",
               "sok.folke.isof.se",
               "sök.folke.isof.se")

# loading manifest, workers, frames, etc
#CSP_FONT_SRC = ("'self'",)
#CSP_CONNECT_SRC = ("'self'","sok.folke.isof.se")
CSP_OBJECT_SRC = ("'self'","sok.folke.isof.se")
#CSP_BASE_URI = ("'self'",)
CSP_FRAME_ANCESTORS = ("'self'","sok.folke.isof.se")
#CSP_FORM_ACTION = ("'self'",)
#CSP_INCLUDE_NONCE_IN = ('script-src',)
#CSP_MANIFEST_SRC = ("'self'",)
#CSP_WORKER_SRC = ("'self'",)
CSP_MEDIA_SRC = ("'self'","sok.folke.isof.se")

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://sok.folke.isof.se",
    "http://forska.folke.isof.se",
    "http://sok.folke-test.isof.se",
    "http://forska.folke-test.isof.se",

]

# Application definition

INSTALLED_APPS = [
    #'Sagenkarta-Admin.apps.SagenkartaDjangoAdminConfig',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'sagenkarta_rest_api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kartplattformen_common.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
            }
        },
    },
]

#WSGI_APPLICATION = 'sagendatabas.wsgi.application'

# Databasesvenska_sagor
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'HOST': secrets_env.host,
        #'PORT': '3306',
        'PORT': secrets_env.port,
        'NAME': secrets_env.database,
        'ENGINE': 'django.db.backends.mysql',
        'USER': secrets_env.user,
        'PASSWORD': secrets_env.passord,
        'OPTIONS': {
          'autocommit': False,
          #'ssl': True
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

#LANGUAGE_CODE = 'sv-se'

#TIME_ZONE = 'UTC+01:00'
TIME_ZONE = 'Europe/Stockholm'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

# MEDIA_ROOT = '/var/www/django/media/'
MEDIA_ROOT = '/home/per/dev/server/sagendatabas/media/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django': {
            # 'handlers': ['console', 'logfile'],
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
            # 'level': 'WARNING',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
        '': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50
}

# *** Settings for HTTPS ***

# Whether to use a secure cookie for the session cookie. Cookie is only sent under an HTTPS connection.
#SESSION_COOKIE_SECURE = True

# Whether to use a secure cookie for the CSRF cookie.
# - Browsers may ensure that the cookie is only sent with an HTTPS connection.
#CSRF_COOKIE_SECURE = True

# ** These settings have no effect if SecurityMiddleware is not enabled! **
# If True, the SecurityMiddleware redirects all non-HTTPS requests to HTTPS (except for those URLs matching
# a regular expression listed in SECURE_REDIRECT_EXEMPT).
#SECURE_SSL_REDIRECT = True

# If a URL path matches a regular expression in this list, the request will not be redirected to HTTPS.
# If SECURE_SSL_REDIRECT is False, this setting has no effect. (Requires SecurityMiddleware).
# - ELAN as of version 4.9.4 does not support HTTPS correctly,
# - therefore the externally controlled vocabulary needs to be served with HTTP.
#SECURE_REDIRECT_EXEMPT = [r'dictionary/ecv/']

# All SSL redirects will be directed to this host rather than the originally-requested host.
# - (Requires SecurityMiddleware  and SECURE_SSL_REDIRECT=True).
#SECURE_SSL_HOST = 'signbank.csc.fi'

# If True, the SecurityMiddleware sets the X-XSS-Protection: 1; mode=block header on all responses that
# do not already have it.
#SECURE_BROWSER_XSS_FILTER = True
