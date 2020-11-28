from functools import wraps

from helper.logger import logger


def debug_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'Call [{func.__name__}], Arguments [{args}, {kwargs}]')
        return func(*args, **kwargs)
    return wrapper
