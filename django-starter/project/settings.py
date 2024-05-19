"""
Django settings for project project.

"""
import os
import sys
from distutils.util import strtobool
from pathlib import Path
from dotenv import dotenv_values
from datetime import timedelta 


config = dotenv_values(".env")

for key, value in config.items():
    os.environ[key] = value

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = 'Um2ga1-#2secret#p!ezs0^!^o#0'
TIME_ZONE = 'Asia/Kolkata'

# Application definition
INSTALLED_APPS = [
    'ramailo.apps.RamailoConfig',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'corsheaders'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000'
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database

POSTGRES_DB=os.environ.get('POSTGRES_DB')
POSTGRES_USER=os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD=os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST=os.environ.get('POSTGRES_HOST')
POSTGRES_PORT=os.environ.get('POSTGRES_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,

    }
}

if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'


SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_SECURE = "true"

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

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATICFILES_DIRS = (('static'),)
STATIC_URL = os.environ.get('STATIC_URL', default='static/')
STATIC_ROOT = os.path.join(BASE_DIR, os.environ.get('STATIC_ROOT', default='static'))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
    ],
}

ENV_ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
ALLOWED_HOSTS = ENV_ALLOWED_HOSTS.split(',') if ENV_ALLOWED_HOSTS is not None else []
DEBUG = bool(strtobool(os.environ.get('DEBUG', default='True')))

# Web URL
WEB_URL = os.getenv("WEB_URL")

#loggers
LOGGING = {
    # Define the logging version
    'version': 1,

    # Enable the existing loggers
    'disable_existing_loggers': False,

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },

    # Define the formatters
    'formatters': {
            'verbose': {
            'format': '[%(levelname)s] [%(asctime)s] [%(module)s] [%(lineno)s] [%(message)s] ',
            },
    },

    # Define the handlers
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs.log',
            'formatter': 'verbose',
            'encoding': 'utf-8'
        },
    },

   # Define the loggers
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': True,
        },

        #database query logger
        # 'django.db.backends': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        # }
    },

}