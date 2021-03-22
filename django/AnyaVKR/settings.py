import os
from pathlib import Path
from google.oauth2 import service_account # noqa
from AnyaVKR.secrets.secrets import DJANGO_SECRET_KEY, DB_PASSWORD # noqa

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = DJANGO_SECRET_KEY

DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'bootstrap_modal_forms',
    'widget_tweaks',
    'phonenumber_field',
    'mainapp.apps.MainappConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'AnyaVKR.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'AnyaVKR.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# [START db_setup]
if os.getenv('GAE_APPLICATION', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '/cloudsql/mercuryschool:europe-north1:my-database',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': DB_PASSWORD,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '127.0.0.1',
            'PORT': '5678',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': DB_PASSWORD,
        }
    }
# [END db_setup]

# Use a in-memory sqlite3 database when testing in CI systems
if os.getenv('TRAMPOLINE_CI', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

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

LANGUAGE_CODE = 'ru-ru'

# TIME_ZONE = 'Etc/GMT-3'
TIME_ZONE = 'Europe/Moscow'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',  # searches in STATICFILES_DIRS
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',  # searches in STATIC subfolder of each app
# ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

X_FRAME_OPTIONS = 'ALLOWALL'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'assets',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_REDIRECT_URL = '/'

CORS_ALLOW_ALL_ORIGINS = True

GS_BUCKET_NAME = 'mercuryschool.appspot.com'
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
# STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    BASE_DIR / "AnyaVKR/secrets/mercuryschool-0c6d566dbefc.json"
)

if DEBUG:
    BOARD_URL = 'http://127.0.0.1:5001'
else:
    BOARD_URL = 'http://35.184.187.225:5001'
