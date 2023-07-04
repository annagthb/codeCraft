"""
Django settings for webDjangoProject project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path
import os
import environ
from dotenv import load_dotenv

env = environ.Env()
environ.Env.read_env()
load_dotenv()
...
# Your secret key
SECRET_KEY = env("SECRET_KEY")
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent#points to the top hierarchy of your site 
                                #whatever paths we define in the project are all relative to BASE_DIR. 
                                #  To use BASE_DIR we will have to use os module provided by Python. 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@ggqq#rbtod%^^^jw#@*k-0jtdss$3efz+)g9pl!=37&+@y19+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG= False

ALLOWED_HOSTS = []#a list having addresses of all domains which can run your Django Project. 
                    #by Default it is 127.0.0.1 or localhost 
                    #When DEBUG set to False 
                    #ALLOWED_HOSTS can not be an empty list. We have to give hosts name in list. i.e. ALLOWED_HOSTS=[“127.0.0.1”, “*.heroku.com”].


# Application definition
#the apps we are going to use for our website
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projectApp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#the urls we check for resolving the website paths
ROOT_URLCONF = 'webDjangoProject.urls'
#ROOT_URLCONF = 'projectApp.urls'

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

WSGI_APPLICATION = 'webDjangoProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/
#default supported db is sqlite3, but many more can be used
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),#or os.environ.get('DB_NAME')
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
        #'OPTIONS':
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'#This variable is used to store the static files. path relative to BASE_DIR
MEDIA_URL='media/'#This variable is used to store the media files.  

STATIC_ROOT= os.path.join(BASE_DIR, 'static')#This variable is used to retrieve the static files. 
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')#This variable is used to retrieve the media files. 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
