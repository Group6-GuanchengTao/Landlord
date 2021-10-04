import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
TEMPLATE_ROOT = os.path.join(BASE_DIR, 'templates')

DEBUG = os.getenv('TORNADO_DEBUG') == 'True'

SECRET_KEY = os.getenv('SECRET_KEY', 'fiDSpuZ7QFe8fm0XP9Jb7ZIPNsOegkHYtgKSd4I83Hs=')

PORT = os.getenv('PORT', 8080)

WECHAT_CONFIG = {
    'appid': os.getenv('APPID'),
    'appsecret': os.getenv('APPSECRET'),
    'token': os.getenv('TOKEN'),
    'encoding_aes_key': os.getenv('ENCODING_AES_KEY'),
}


def database_url(url):
    from urllib.parse import urlparse, ParseResult
    pr: ParseResult = urlparse(url)
    return {
        'host' : pr.hostname,
        'database': pr.path[1:],
        'user': pr.username,
        'password': pr.password,
    }


DATABASE = database_url(os.getenv('DATABASE_URL', 'mysql://scbmflfyvcca6t02:q7pyshtonwzl0inv@phtfaw4p6a970uc0.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/ec75y76mnx21m5bi'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
        'propagate': True,
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'tornado.general': {
            'handlers': ['console'],
            'propagate': True,
        },
    }
}
