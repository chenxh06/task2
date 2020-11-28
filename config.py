import os
from pathlib import Path


class Config:
    # path
    PROJECT_DIR = Path(os.path.dirname(__file__))
    LOG_DIR = str(PROJECT_DIR / Path('log'))
    REPORT_DIR = str(PROJECT_DIR / Path('allure-report/'))
    RESULT_DIR = str(PROJECT_DIR / Path('allure-results'))
    TESTCASE_DATA_DIR = str(PROJECT_DIR / Path('data/test_data.yml'))

    # logger
    LOGGER = 'dev'
    DEFAULT_LOG_LEVEL = 'INFO'

    # response code
    CODE_SUCCESS = 200