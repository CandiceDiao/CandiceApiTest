import json
from typing import List
import pytest
from pip._vendor.lockfile import FileLock

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

# #获取token值
# @pytest.fixture(scope="session")
# def token():
#     print("这是获取token方法")
#     data = BaseApi.load_yaml('token.yaml')
#     token = Token().get_token(data)
#     yield token

# 解决并发测试时：fixture  scope= session不起作用的
@pytest.fixture(scope='session')
def token(tmp_path_factory, worker_id):
    """
    解决并发测试时：fixture （scope= session）不起作用的
    :param tmp_path_factory:临时文件夹路径
    :param worker_id:进程id
    :return:token值
    """
    if not worker_id:
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        data_token = BaseApi.load_yaml('token.yaml')
        yield Token().get_token(data_token)

    # get the temp directory shared by all workers
    # tmp_path_factory:是一个session范围的fixture,可用于从任何其他测试用例及fixture中创建任意临时目录。
    # 例如：root_tmp_dir=C:\Users\WBPC0154\AppData\Local\Temp\pytest-of-WBPC0154\pytest-19
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data.json"

    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            # 之后的进程进行读文件操作，拿到token值
            data = json.loads(fn.read_text())
        else:
            data_token = BaseApi.load_yaml('token.yaml')
            data = Token().get_token(data_token)
            # 第一次执行将token值写入文件data.josn.lock
            fn.write_text(json.dumps(data))
    yield data

