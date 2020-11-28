import pytest
import requests

from config import Config
from helper.loader import CaseLoader
from helper.logger import logger
from helper.utils import function_name, day_after_tomorrow


@pytest.mark.usefixtures('host')
class TestHumidity:

    def test_humidity(self, host):
        data = CaseLoader().load()['test case'][function_name()]
        r = requests.request(data['request']['method'],
                             url=host+data['request']['url'],
                             headers=data['request']['headers'])
        logger.info(r.status_code)
        assert r.status_code == Config.CODE_SUCCESS
        res = self.get_humidity_of_day_after_tomorrow(r)

        logger.info(f'Day after tomorrow: {res["forecast_date"]}')

        # extract relative humidity
        logger.info(f'Relative humidity: {res["min_rh"]}% - {res["max_rh"]}%')

        # assert forecast_date is the day after tomorrow
        assert res['forecast_date'] == day_after_tomorrow()

    @staticmethod
    def get_humidity_of_day_after_tomorrow(r):
        response = r.json()
        # 2nd item of forecast_detail dict contains the data of day after tomorrow
        return response['forecast_detail'][1]
