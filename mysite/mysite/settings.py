# Django settings for mysite project.
#encoding=utf8
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'easy_drive',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'joker',
        'PASSWORD': 'likejoke',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
#TIME_ZONE = 'America/Chicago'
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'

LANGUAGE_CODE = 'zh-CN'
LANGUAGES = (('zh-cn', u'简体中文'), # instead of 'zh-CN'
                 ('zh-tw', u'繁體中文'), # instead of 'zh-TW'
                         )

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

import os
if os.environ.has_key('MYSITE_ROOT'):
	WORK_ROOT = os.environ['MYSITE_ROOT']
else:
	WORK_ROOT="/home/lxwsj/zhuyc/mysite"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = WORK_ROOT+'/media/'
CKEDITOR_UPLOAD_PATH = WORK_ROOT + "/media/"
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = WORK_ROOT + '/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    WORK_ROOT + '/static/admin',
    WORK_ROOT + '/static/ckeditor',
#    WORK_ROOT + '/static/djangobb_forum',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'v_zy^ostcjfqh%qr_=w!8&u&pwe76iw+l^8cgge!zaps%ni9)o'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mysite.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    WORK_ROOT + '/templates',

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'registration',
#    'drive',
    'ckeditor',
  #  'djangobb_forum',
    'pagination',
  #  'dbe',
  #  'blog',
  #  'photo',
    'forum',
    # Uncomment the next line to enable the admin:
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)
CKEDITOR_RESTRICT_BY_USER=True
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGIN_REDIRECT_URL='/drive/coach/update/'
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

CKEDITOR_CONFIGS = {
        'awesome_ckeditor': {
            'toolbar': 'Basic',
            },
        'default': {
            'toolbar': 'Full',
            'height': 200,
            'width': 400,
            },
        }

HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
            'URL': 'http://localhost:9001/solr/default',
            'TIMEOUT': 60 * 5,
            'INCLUDE_SPELLING': True,
            'BATCH_SIZE': 100,
            'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
            },
        'autocomplete': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            'PATH': '/home/search/whoosh_index',
            'STORAGE': 'file',
            'POST_LIMIT': 128 * 1024 * 1024,
            'INCLUDE_SPELLING': True,
            'BATCH_SIZE': 100,
            'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
            },
        'slave': {
            'ENGINE': 'xapian_backend.XapianEngine',
            'PATH': '/home/search/xapian_index',
            'INCLUDE_SPELLING': True,
            'BATCH_SIZE': 100,
            'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
            },
        'db': {
            'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
            'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
            }
        }
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'wuyou1979@gmail.com'
EMAIL_HOST_PASSWORD = 'Zhuyc9918'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = "Easy Drive <wuyou1979@gmail.com>"
SERVER_EMAIL = "wuyou1979@163.com"


ACCOUNT_ACTIVATION_DAYS=7
