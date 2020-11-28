import pytest

from helper.loader import CaseLoader


@pytest.fixture(scope='class', autouse=True)
def host(request):
    return CaseLoader().load()['host']
