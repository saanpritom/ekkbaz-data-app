"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os
import environ


# Initialize the environment variable file.
env = environ.Env(
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent

# Set the environment file path.
environ.Env.read_env(os.path.join(ROOT_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('BUSINESS_APP_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('BUSINESS_APP_DEBUG')

ALLOWED_HOSTS = env.list('BUSINESS_APP_ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'apps.business',
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

ROOT_URLCONF = 'conf.urls'

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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env.str('BUSINESS_APP_DATABASE_ENGINE'),
        'NAME': env.str('BUSINESS_APP_DATABASE_NAME'),
        'USER': env.str('BUSINESS_APP_DATABASE_USER'),
        'PASSWORD': env.str('BUSINESS_APP_DATABASE_PASSWORD'),
        'HOST': env.str('BUSINESS_APP_DATABASE_HOST'),
        'PORT': env.int('BUSINESS_APP_DATABASE_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# DRF Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': env.int('BUSINESS_APP_LIST_API_PAGE_SIZE'),
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = env.str('BUSINESS_APP_LANGUAGE_CODE')

TIME_ZONE = env.str('BUSINESS_APP_TIME_ZONE')

USE_I18N = env.bool('BUSINESS_APP_USE_I18N')

USE_TZ = env.bool('BUSINESS_APP_USE_TZ')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=env.int('BUSINESS_APP_ACCESS_TOKEN_LIFETIME_MINUTES')),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=env.int('BUSINESS_APP_REFRESH_TOKEN_LIFETIME_MINUTES')),
    'ROTATE_REFRESH_TOKENS': env.bool('BUSINESS_APP_ROTATE_REFRESH_TOKENS'),
    'BLACKLIST_AFTER_ROTATION': env.bool('BUSINESS_APP_BLACKLIST_AFTER_ROTATION'),
    'UPDATE_LAST_LOGIN': env.bool('BUSINESS_APP_UPDATE_LAST_LOGIN'),

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': env.str('BUSINESS_APP_SIGNING_KEY'),
    'VERIFYING_KEY': env.str('BUSINESS_APP_VERIFYING_KEY'),
    'AUDIENCE': env.str('BUSINESS_APP_AUDIENCE'),
    'ISSUER': env.str('BUSINESS_APP_ISSUER'),
    'JWK_URL': None,
    'LEEWAY': env.int('BUSINESS_APP_LEEWAY_MINUTES'),

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=env.int('BUSINESS_APP_SLIDING_TOKEN_LIFETIME_MINUTES')),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(minutes=env.int('BUSINESS_APP_SLIDING_TOKEN_REFRESH_LIFETIME_MINUTES')),
}
