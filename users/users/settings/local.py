from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# Le indicamos a Django el directorio de los archivos estáticos
STATICFILES_DIRS = [BASE_DIR.child('static')]

# Media files
MEDIA_URL = '/media/'
# Indicamos la carpeta raíz en donde estarán almacenados los archivos multimedia
MEDIA_ROOT = BASE_DIR.child('media')