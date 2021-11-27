from __future__ import absolute_import, unicode_literals

import datetime
from pathlib import Path

import environ

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('src')
ENV_PATH = str(APPS_DIR.path('.env'))

env = environ.Env()
if env.bool('READ_ENVFILE', default=True):
    env.read_env(ENV_PATH)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=['localhost'])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'drf_yasg',
    'conferences',
    'participants',
    'talks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASE_URL = 'sqlite:///wp-api.db'
POSTGRES_DB = env('POSTGRES_DB', default=None)
POSTGRES_USER = env('POSTGRES_USER', default=None)
POSTGRES_PASSWORD = env('POSTGRES_PASSWORD', default=None)
POSTGRES_SERVICE = env('POSTGRES_SERVICE', default=None)
if POSTGRES_DB and POSTGRES_USER and POSTGRES_PASSWORD and POSTGRES_SERVICE:
    DATABASE_URL = 'postgres://' + POSTGRES_USER + ':' + POSTGRES_PASSWORD + POSTGRES_SERVICE + POSTGRES_DB

DATABASES = {
    'default': env.db('POSTGRES_DATABASE_URL', default=DATABASE_URL),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = 600


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer', ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': env.int("PAGINATION_PAGE_SIZE", default=10)
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=2),
}
