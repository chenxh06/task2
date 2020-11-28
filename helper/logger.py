import logging.config
import time
from pathlib import Path

from config import Config

log_path = str(Config.LOG_DIR / Path(time.strftime('%Y%m%d-%H%M%S', time.localtime()))) + '.log'
Path(Config.LOG_DIR).mkdir(parents=True, exist_ok=True)
Path(log_path).touch()

logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug': {
            'format': '%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'info': {
            'format': '%(asctime)s [%(levelname)8s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'debug',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'debug',
            'maxBytes': 10485760,
            'backupCount': 20,
            'encoding': 'utf8',
            'filename': log_path
        }
    },
    'loggers': {
        Config.LOGGER: {
            'level': Config.DEFAULT_LOG_LEVEL,
            'handlers': ['console', 'file'],
            'propagate': False
        }
    }
}


logging.config.dictConfig(logger_config)
logger = logging.getLogger(Config.LOGGER)
