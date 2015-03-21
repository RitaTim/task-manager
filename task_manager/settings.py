"""
Django settings for task_manager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mrya1(&4p9n=)n%+qgf8fpq9x1n3)ugdy1(v^ei1-mweys86yn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
                r'/home/rita/Documents/task_manager/task_manager/templates',
                r'/home/rita/Documents/task_manager/project/templates',
                r'/home/rita/Documents/task_manager/auth/templates',
                r'/home/rita/Documents/task_manager/task/templates',
)

ALLOWED_HOSTS = []

#AUTH_USER_MODEL = 'auth.User'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.formtools',
    'django.utils.log',
    'debug_toolbar',
    'django.contrib.staticfiles',
    'auth',
    'bootstrapform',
    'south',
    'dajax',
    'dajaxice',
    'task',
    'project',
    'comment',
    'forum',
    'iteration',
    'user_profile',
    'jquery'
)

AUTH_PROFILE_MODEL = 'user_profile.UserProfile'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'task_manager.urls'

WSGI_APPLICATION = 'task_manager.wsgi.application'

LOGIN_REDIRECT_URL = '/projects'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #'django.db.backends.sqlite3',
        'NAME': 'django_db', #os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

MEDIA_ROOT = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'media',
)

MEDIA_URL  = '/media/'

#STATIC_ROOT = '/home/rita/Documents/task_manager/static/'

STATICFILES_DIRS =(
    r'/home/rita/Documents/task_manager/static/',
)

STATIC_URL = '/static/'

#CASHE
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 86400,
    }
}