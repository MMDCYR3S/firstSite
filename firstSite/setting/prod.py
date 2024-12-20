from firstSite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-otgm9$tbzpg8n81#1^$)n2zy7@5@ao-p0468g#0vp-06yre5fh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["cyr3s.pythonanywhere.com"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Define Site ID(Site Framework)
SITE_ID = 1

#
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]

MEDIA_ROOT = BASE_DIR / 'media'

# Define CSRF Cookie Secure
CSRF_COOKIE_SECURE = True
