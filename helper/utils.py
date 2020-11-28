import datetime
import inspect
import time


def current_time():
    return time.strftime('%Y%m%d-%H%M%S', time.localtime())


def day_after_tomorrow():
    return (datetime.date.today() + datetime.timedelta(days=2)).strftime('%Y%m%d')


def function_name():
    return inspect.getouterframes(inspect.currentframe())[1].function
