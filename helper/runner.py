import argparse
import os
from pathlib import Path

import pytest

from config import Config
from helper.utils import current_time


class Parser:
    def __init__(self):
        self.args = None
        self.parser = argparse.ArgumentParser()
        self.add_option()

    def add_option(self):
        self.add_case_option()

    def add_case_option(self):
        self.parser.add_argument(
            '--test',
            type=str,
            default='test_case',
            help='test case path'
        )

    def get_args(self, options=None):
        self.args = self.parser.parse_args(options)
        return self.args


class Runner:
    def __init__(self):
        self.pytest_args = []
        self.args = Parser().get_args()
        if self.args.test:
            print(self.args.test)
        self.allure_results_dir = Config.RESULT_DIR / Path(current_time())

    def create_allure_dir(self):
        if not Path(self.allure_results_dir).is_dir():
            Path(self.allure_results_dir).mkdir(parents=True, exist_ok=True)
        if not Path(Config.REPORT_DIR).is_dir():
            Path(Config.REPORT_DIR).mkdir(parents=True, exist_ok=True)

    def append_pytest_args(self):
        # cli log output
        # self.pytest_args.append('-s')
        # test case path
        self.pytest_args.append(self.args.test)
        # allure dir
        self.pytest_args.append(f'--alluredir={self.allure_results_dir}')

    def start(self):
        self.append_pytest_args()
        print(self.pytest_args)
        self.create_allure_dir()
        pytest.main(self.pytest_args)
        self.generate_report()

    def generate_report(self):
        os.system(f'allure generate {self.allure_results_dir} -o {Config.REPORT_DIR} --clean')


if __name__ == '__main__':
    Runner().start()
