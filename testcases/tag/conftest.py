import pytest

from api.wework import Token
from api.base_api import BaseApi

# 获取token值
@pytest.fixture(scope="session")
def token():
    data = BaseApi.load_yaml('token.yaml')
    token = Token().get_token(data)
    yield token
