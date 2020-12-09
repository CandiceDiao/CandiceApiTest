"""
所有api类的父类，实现了各种有用的方法
"""
import os
from string import Template

import requests
import yaml

from utils.config import DATA_PATH


class BaseApi:

    #发送请求
    def send_api(self,data:dict):
        res=requests.request(**data)
        return res

    #读取yaml文件,返回python数据类型
    #在conftest.py中调用时使用类名直接调用，不用生成对象；所以讲该方法定义为类方法
    @classmethod
    def load_yaml(cls,ymlname):
        path = os.path.join(DATA_PATH, ymlname)
        with open(path) as f:
            return yaml.safe_load(f)

    #模板技术
    def template(self, ymlname, data, sub=None):
        path = os.path.join(DATA_PATH, ymlname)
        with open(path) as f:
            if sub is None:
                return yaml.safe_load(Template(f).substitute(data))
            else:
                return yaml.safe_load(Template(yaml.dump(yaml.safe_load(f)[sub])).substitute(data))











