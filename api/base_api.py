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
    def load_yaml(cls,ymlname,sub=None):
        """
        封装yaml读取的代码，通过路径直接读取yml文件并转化成python数据类型
        :param path: yml文件的相对路径
        :param sub: 读取yml文件的二级数据目录，默认为None
        :return: 返回yml文件的python数据
        """
        path = os.path.join(DATA_PATH, ymlname)
        with open(path,encoding="utf-8") as f:
            if sub is None:
                return yaml.safe_load(f)
            else:
                return yaml.safe_load(f)[sub]

    #模板技术
    def template(self, ymlname, data, sub=None):
        path = os.path.join(DATA_PATH, ymlname)
        with open(path,encoding="utf-8") as f:
            if sub is None:
                return yaml.safe_load(Template(f).substitute(data))
            else:
                return yaml.safe_load(Template(yaml.dump(yaml.safe_load(f)[sub])).substitute(data))











