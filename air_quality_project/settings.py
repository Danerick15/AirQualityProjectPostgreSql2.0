import os 
from pathlib import Path
import dj_database_url  # pip install dj-database-url

from dotenv import load_dotenv
load_dotenv()

# Rutas base
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-+%zijn7bq6ndi9(j0$v@qsxw&b@-49)w^qm1hh&@7272h9xnm=")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".onrender.com"]

# Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'sensores',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  #  WhiteNoise para servir archivos estáticos

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'air_quality_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'air_quality_project.wsgi.application'

# Base de datos (adaptable: Render con SSL, local sin SSL)
if os.getenv("RENDER", "") == "true":
    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': dj_database_url.config(
            default="postgresql://postgres:xis@localhost:5432/air_quality_db",
            conn_max_age=600,
            ssl_require=False
        )
    }

# Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
] 

# Localización
LANGUAGE_CODE = 'en-us' 
TIME_ZONE = 'America/Lima' 
USE_I18N = True 
USE_TZ = True  

# Archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Clave por defecto para los modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' 