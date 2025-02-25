from pathlib import Path
from django.conf import ENVIRONMENT_VARIABLE
from dotenv import load_dotenv
import environ
import os
import dj_database_url
from decouple import config

# from environ import ENV
load_dotenv()
env = environ.Env()
environ.Env.read_env()
ENVIRONMENT = env('ENVIRONMENT', default = 'development')

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY")

if ENVIRONMENT == 'development':
    DEBUG = True
else :
    DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'https://fitnessapp-production-cf6d.up.railway.app/']

CORS_ALLOWED_ORIGINS = [
    'https://fitnessapp-production-cf6d.up.railway.app',
    'http://localhost:3000',
    'http://127.0.0.1:9000'
]


CSRF_TRUSTED_ORIGINS = [
    'https://fitnessapp-production-cf6d.up.railway.app',
    "http://localhost:3000",
    "http://127.0.0.1:9000",
]

CORS_ALLOW_ALL_ORIGINS = True

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'rest_framework',
    'drf_spectacular',
    'corsheaders',
]


REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ],
    # for documing api
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Enable Whitenoise   
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'Backend.urls'

WSGI_APPLICATION = "Backend.wsgi.application"

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

DATABASES = {
'default': dj_database_url.config(
    default=config('DATABASE_URL', default = os.getenv("DATABASE_URL"))
)
}

# POSTGRES_LOCALLY = env('POSTGRES_LOCALLY') == 'True'
# DATABASE_URL = os.getenv('DATABASE_URL')

# if ENVIRONMENT == 'production' or POSTGRES_LOCALLY:
#     if DATABASE_URL:
#         DATABASES['default'] = dj_database_url.parse(DATABASE_URL)
#     else:
#         print("Warning: DATABASE_URL not found in environment variables")

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'