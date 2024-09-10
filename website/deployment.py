import os
from .settings import *
from . settings import BASE_DIR


SECRET_KEY = os.environ['SECRET_KEY','dBmRu7qaYjbSANVwoE0!p&n31']

ALLOWED_HOSTS = [os.environ['azurewebapp-fvdbgagvgyghd6eu.centralindia-01.azurewebsites.net','localhost']]
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['azurewebapp-fvdbgagvgyghd6eu.centralindia-01.azurewebsites.net','localhost']]
DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING','']
parameters = {pair.split('=')[0]:pair.split('=')[1] for pair in connection_string.split(' ')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parameters['dbname'],
        'HOST':parameters['host'],
        'USER': parameters['user'],
        'PASSWORD':parameters['password'],
    }
}