from typing import List

# 解决参数中带有中文的编码问题
import pytest

from api.base_api import BaseApi
from api.wework import Token


def pytest_collection_modifyitems(
        session:"Session",config:"Config",items:List["Item"]
)->None:
    # items所有测试用例列表，item 代表每一个测试用例
    # 用例执行顺序颠倒
    items.reverse()

    for item in items:
        # 解决参数中带有中文的编码问题：
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid=item.nodeid.encode('utf-8').decode('unicode-escape')

# 获取token值
@pytest.fixture(scope="session")
def token():
    data = BaseApi.load_yaml('token.yaml')
    token = Token().get_token(data)
    yield token