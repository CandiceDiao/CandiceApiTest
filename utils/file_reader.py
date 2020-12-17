"""
用于文件的读取
包含配置文件和数据文件的读取函数.根据文件地址，返回文件中包含的内容
"""
import os
from string import Template
import yaml

from utils.config import DATA_PATH


class YamlReader:

    def __init__(self,yamlfilepath):
        yamlfilepath = os.path.join(DATA_PATH, yamlfilepath)
        if os.path.exists(yamlfilepath):
            self.yamlpath = yamlfilepath
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None


    #读取yaml文件,返回python数据类型
    #在conftest.py中调用时使用类名直接调用，不用生成对象；所以讲该方法定义为类方法
    def load_yaml(self,sub=None):
        """
        封装yaml读取的代码，通过路径直接读取yml文件并转化成python数据类型
        :param path: yml文件的相对路径
        :param sub: 读取yml文件的二级数据目录，默认为None
        :return: 返回yml文件的python数据
        """
        with open(self.yamlpath,encoding="utf-8") as f:
            if sub is None:
                return yaml.safe_load(f)
            else:
                return yaml.safe_load(f)[sub]

    #模板技术
    def template(self, data, sub=None):
        """
        使用模板技术，把yml文件中的变量进行二次转化，是本框架的yml文件的技术基础
        :param path: 模板技术输入yml文件相对路径
        :param data: data是需要修改的模板变量的字典类型
        :param sub: sub是对yml的数据进行二次提取，等于是一个大字典，再提取下一层的小字典，为了让一个yml文件可以有多个接口数据
        :return:
        """
        with open(self.yamlpath,encoding="utf-8") as f:
            if sub is None:
                return yaml.safe_load(Template(f).substitute(data))
            else:
                return yaml.safe_load(Template(yaml.dump(yaml.safe_load(f)[sub])).substitute(data))

# 读取excel文件中的内容。返回list。待补充
class ExcelReader:
    pass