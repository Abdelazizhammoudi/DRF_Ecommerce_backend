import os
from .settings import *
from .settings import BASE_DIR
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME' ]]
CSRF TRUSTED ORIGINS ['https://'+os.environ['WEBSITE_HOSTNAME']]
SECRET_KEY = os.environ['MY_SECRET_KEY']
DEBUG = False



MIDDLEWARE = [
    # Security middleware
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    # Django core middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "https://sm-shope.netlify.app",
    "https://sm-shop.onrender.com",
]

STORAGES = {
"default": {
"BACKEND": "django.core.files.storage. FileSystemStorage",
},
"staticfiles": {
"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
}, I
}

# Production PostgreSQL configuration
CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING"]
CONNECTION_STR = {pair.split('=')[0]: pair.split('=')[1] for pair in CONNECTION.split(' ')}

DATABASES = {
        "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": CONNECTION_STR['dbname'],
        "HOST" CONNECTION_STR['host'],
        "USER": CONNECTION_STR['user'],
        "PASSWORD": CONNECTION_STR['password'],
        "PORT": CONNECTION_STR['port'],
        }
} 

STATIC_ROOT = BASE_DIR/'staticfiles'