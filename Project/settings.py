from pathlib import Path
import os
from decouple import config

# Base directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for production (use environment variable or config)
SECRET_KEY = config('SECRET_KEY')

# Debug mode (don't use in production)
DEBUG = config('DEBUG', default=True, cast=bool)

# Allowed hosts for production
ALLOWED_HOSTS = ['.vercel.app']

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # Custom Apps
    'app', 
    'employe',
    'leave',
    'profiles',
    'admins',
    'checkin',
]

# Middleware for security, sessions, etc.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Root URL configuration
ROOT_URLCONF = "Project.urls"

# Templates configuration
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Custom template directory
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI application for deployment
WSGI_APPLICATION = "Project.wsgi.application"

# Database configuration (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),  
        'USER': config('DB_USER'), 
        'PASSWORD': config('DB_PASSWORD'), 
        'HOST': config('DB_HOST'),  
        'PORT': config('DB_PORT', default='5432'),  
    }
}

# Password validators (standard Django validators)
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Localization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True  # Enable timezone support

# Static files configuration
STATIC_URL = '/static/'

# Change STATIC_ROOT to store collected static files for production
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory for static files after collectstatic

# The directory where static files are during development
STATICFILES_DIRS = [BASE_DIR / "static"]  # Your local static folder

# Media files (uploads)
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
