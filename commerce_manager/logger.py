import logging.config

from commerce_manager.settings import Config


LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            "format": "%(levelname)s [%(name)s:%(process)d:%(lineno)d] %(asctime)s %(message)s",
        },
    },
    'handlers': {
        'console': {
            'formatter': "default",
            'class': "logging.StreamHandler",
            'stream': "ext://sys.stdout"
        }
    },
    'loggers': {
        '': {
            'level': Config.log_level,
            'handlers': ['console'],
        },
        'shop_services': {
            'level': Config.log_level,
            'handlers': ['console'],
            'propagate': False
        },
        'gunicorn': {
            'level': logging.INFO,
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('shop_services')
