import os
from ConfigParser import RawConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR_LOGS = os.path.join(BASE_DIR, 'logs')

# Config
config = RawConfigParser()
config.read(os.path.join(BASE_DIR, 'settings.ini'))

SECRET_KEY = config.get('secrets', 'SECRET_KEY')

DEBUG = False if config.get('environment', 'ENVIRONMENT') == "PRODUCTION" else True
TEMPLATE_DEBUG = False if config.get('environment', 'ENVIRONMENT') == "PRODUCTION" else True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'slackrandom'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_project.urls'

WSGI_APPLICATION = 'django_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE':config.get('database', 'DATABASE_ENGINE'),
        'NAME': config.get('database', 'DATABASE_NAME'),
        'USER': config.get('database', 'DATABASE_USER'),
        'PASSWORD': config.get('database', 'DATABASE_PASSWORD'),
        'HOST': config.get('database', 'DATABASE_HOST'),
        'PORT': config.get('database', 'DATABASE_PORT'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR_LOGS, 'slackrandom.log'),
        },
        'slackrandomerror': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR_LOGS, 'slackrandomerror.log'),
        },
        'slackrandomrequest': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR_LOGS, 'slackrandomrequest.log'),
        },
    },
    'loggers': {
        'slackrandom.info': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'slackrandom.error': {
            'handlers': ['slackrandomerror'],
            'level': 'ERROR',
            'propagate': True,
        },
        'slackrandom.request': {
            'handlers': ['slackrandomrequest'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

APPEND_SLASH = False

# Redis
REDIS_ENABLED = True
REDIS_SOCK = '/var/run/redis/redis.sock'
REDIS_BYTES_GENERATED = 'BYTES_GENERATED'
REDIS_REQUEST_COUNT = 'REQUEST_COUNT'

# SlackRandom urls
SLACKRANDOM_URL_HOME = 'http://slackrandom.com'
SLACKRANDOM_URL_API_RANDOM = SLACKRANDOM_URL_HOME + '/random'
SLACKRANDOM_URL_GITHUB = 'https://github.com/strattonw/slackrandom'
