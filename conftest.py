import pytest

from core.api.base_client import BaseApiClient


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='session')
def api_client(base_url):
    return BaseApiClient(base_url)


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://reqres.in/api/", help="This is request url")
