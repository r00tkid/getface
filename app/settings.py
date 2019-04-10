import os, datetime
from configurations import Configuration


class Development(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    [LOGS_DIR] = os.path.abspath(os.path.join(BASE_DIR, 'project', 'log')),
    DEFAULT_NAME = "Get Face"
    BASE_URL = "http://127.0.0.1:9090"

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
    APPEND_SLASH = False
    # SILENCED_SYSTEM_CHECKS = ['models.E006']
    # urls.W002 - if APPEND_SLASH in True silence warnings for routes without slashes

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '7751c0)##x&(z94r6*h9076d5izvo#)6-dj3_sor!6i8f5pnl#'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '::1']

    # Mail settings
    EMAIL_HOST_PASSWORD = 'getface-85Ftww34'
    EMAIL_HOST_USER = 'admin@get-face.com'
    EMAIL_HOST = 'get-face-mail'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False

    EMAIL_ADDRESSES = {
        'main': 'Get Face official <no-response@get-face.com>',
        'admin': 'Get Face administrator <admin@get-face.com>',
        'finance': 'Get Face financial <finance@get-face.com>',
        'info': 'Get Face info <info@get-face.com>',
    }

    # Application definition
    FAKER_LOCALE = None  # settings.LANGUAGE_CODE is loaded
    FAKER_PROVIDERS = None  # faker.DEFAULT_PROVIDERS is loaded (all)

    INSTALLED_APPS = [
        'django.contrib.contenttypes',
        'django.contrib.staticfiles',

        'bootstrap_admin',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.auth',

        'django_extensions',

        'rest_framework',
        'rest_framework_jwt',

        'entry.apps.AuthenticationConfig',
        'holding.apps.HoldingConfig',
        'job.apps.JobConfig',
        'pay.apps.PaymentConfig',
        'cam.apps.CameraConfig',
    ]

    AUTH_USER_MODEL = 'auth.User'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'django_debug': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGS_DIR, 'debug.log'),
            },
            'django_info': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGS_DIR, 'django.log'),
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },

        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{asctime} [{levelname}] {message}',
                'style': '{',
            },
        },

        'loggers': {
            'django': {
                'handlers': ['console', 'django_info'],
                'level': 'INFO',
                'propagate': True,
            },
            'debug': {
                'handlers': ['console', 'django_debug'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

    REST_FRAMEWORK = {
        'UNAUTHENTICATED_USER': None,
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
    }

    JWT_AUTH = {
        'JWT_ENCODE_HANDLER':
            'rest_framework_jwt.utils.jwt_encode_handler',

        'JWT_DECODE_HANDLER':
            'rest_framework_jwt.utils.jwt_decode_handler',

        'JWT_PAYLOAD_HANDLER':
            'rest_framework_jwt.utils.jwt_payload_handler',

        'JWT_PAYLOAD_GET_USER_ID_HANDLER':
            'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

        'JWT_RESPONSE_PAYLOAD_HANDLER':
            'rest_framework_jwt.utils.jwt_response_payload_handler',

        'JWT_SECRET_KEY': SECRET_KEY,
        'JWT_GET_USER_SECRET_KEY': None,
        'JWT_PUBLIC_KEY': None,
        'JWT_PRIVATE_KEY': None,
        'JWT_ALGORITHM': 'HS256',
        'JWT_VERIFY': True,
        'JWT_VERIFY_EXPIRATION': True,
        'JWT_LEEWAY': 0,
        'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=12),
        'JWT_AUDIENCE': None,
        'JWT_ISSUER': None,

        'JWT_ALLOW_REFRESH': True,
        'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

        'JWT_AUTH_HEADER_PREFIX': 'Bearer',
        'JWT_AUTH_COOKIE': None,
    }

    MIDDLEWARE = [
        'index.middleware.SimpleMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ]

    ROOT_URLCONF = 'index.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'static'),
                os.path.join(BASE_DIR, 'templates'),
            ],
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

    TEMPLATE_PREFIXES = {
        'mail': 'mail',  # For e-mail templates
        'page': 'page',  # For pages that are not in SPA
    }

    WSGI_APPLICATION = 'index.wsgi.get_face'

    # Database
    # https://docs.djangoproject.com/en/2.1/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'get_face_stage',
            'HOST': 'get-face-stage-db',
            'PORT': '5432',
            'USER': 'root',
            'PASSWORD': '123456',
            'DEFAULT_CHARSET': 'utf8mb4',
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/2.1/topics/i18n/

    LANGUAGE_CODE = 'ru-ru'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.1/howto/static-files/

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'project', 'assets', 'dist')
    ]

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'project', 'media')
    MEDIA_URL = '/media/'


class Production(Development):
    DEBUG = False

    # ToDo: change on real site base
    BASE_URL = "http://159.89.28.40:9090"
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '::1', '159.89.28.40']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'get_face_prod',
            'HOST': 'get-face-db',
            'PORT': '5432',
            'USER': 'root',
            'PASSWORD': '123456',
            'DEFAULT_CHARSET': 'utf8mb4',
        }
    }
