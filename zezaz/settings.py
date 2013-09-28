# Django settings for zezaz project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

gettext = lambda s: s
PROJECT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(PROJECT_DIR)

ADMINS = (
    ('Ezequiel Bertti', 'ebertti@gmail.com'),
    ('Joao Leite', 'joaoleite@gmail.com'),
    ('Cesar Frias', 'cegfrias@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'zezaz.db',
    }
}

ALLOWED_HOSTS = ['zezaz.amazingworks.com.br']

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, 'static/media/')
STATIC_URL = '/static/collect/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'static/collect/')
TEMPLATE_DIRS = (os.path.join(ROOT_DIR, 'templates/'),)

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '3g2-s^&7u=a(9%(*#3b1g2d$5)0xne-)pk#v2_6bd=8$*^af)c'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'zezaz.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'zezaz.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',
    'recomendation',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
