import os
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]

# 将 D:\PycharmProjects\luffy_api\luffy_api\apps 放入环境变量
sys.path.insert(0, str(BASE_DIR / 'apps'))

# 将 D:\PycharmProjects\luffy_api\luffy_api 放入环境变量
sys.path.insert(0, str(BASE_DIR))

SECRET_KEY = 'django-insecure-j9ubk42ym0whw%mjxi$+e+_wxr)%pi!y4tzi0!u8=m6pmri3(f'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'home',
    'user',
    'course',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'luffy_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'luffy_api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'luffy',
        'USER': os.environ.get('MYSQL_USER', 'kongjie'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', '123456789'),
        'HOST': '127.0.0.1',
        'PORT': '3306'
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = False

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            # 实际开发建议使用WARNING
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # 实际开发建议使用ERROR
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建，注：这里的文件路径要注意BASE_DIR代表的是小luffyapi
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs", "luffy.log"),
            # 日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 文件内容编码
            'encoding': 'utf-8'
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'luffy_api.utils.common_exception_handler.common_exception_handler'
}

AUTH_USER_MODEL = 'user.User'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 跨域问题配置
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
    'token',
    'Cache-Control',
)

# 20 simpleui的配置
# 配置主题
# SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'

# 去掉菜单图标
# SIMPLEUI_DEFAULT_ICON = False

# 自定图标
# SIMPLEUI_ICON = {'首页功能': 'fab fa-apple',}

# 自定义菜单

SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menu_display': ['首页功能', '用户管理', '权限认证', '课程管理', '我们的测试'],
    # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,  # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [
        {
            'name': '首页功能',
            'icon': 'fas fa-code',
            'models': [
                {
                    'name': '轮播图管理',
                    'icon': 'fa fa-user',
                    'url': 'home/banner/'
                },
            ]

        },
        {
            'name': '用户管理',
            'icon': 'fas fa-code',
            'models': [
                {
                    'app': 'user',
                    'name': '用户',
                    'icon': 'fa fa-user',
                    'url': 'user/user/'
                },
            ]

        },

        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '组管理',
                    'icon': 'fa fa-user',
                    'url': 'auth/group/'
                },
            ]
        },
        {
            'name': '课程管理',
            'icon': 'fas fa-code',
            'models': [
                {
                    'name': '课程分类',
                    'icon': 'fa fa-user',
                    'url': 'course/coursecategory/'
                },
                {
                    'name': '课程',
                    'icon': 'fa fa-user',
                    'url': 'course/course/'
                },
                {
                    'name': '教师',
                    'icon': 'fa fa-user',
                    'url': 'course/teacher/'
                },
                {
                    'name': '章节',
                    'icon': 'fa fa-user',
                    'url': 'course/coursechapter/'
                },
                {
                    'name': '课时',
                    'icon': 'fa fa-user',
                    'url': 'course/coursesection/'
                },
            ]

        },
        # {
        #
        #     'name': '我们的测试',
        #     'icon': 'fas fa-user-shield',
        #     'url': '/demo'
        # },
    ]
}

from .common_settings import *

# 缓存设置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
            # "PASSWORD": "123",
        }
    }
}
