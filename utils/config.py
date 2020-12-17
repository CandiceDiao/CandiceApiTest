'''
读取config文件
'''
import configparser
import os


# os.path.abspath(__file__) 返回脚本的绝对路径
# os.path.dirname(path) 返回path父路径
# os.path.split() -》返回tuple （输出路径，文件名） 所以要去tuple[0]
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
#将 data 文件夹拼接到输出路径下
DATA_PATH = os.path.join(BASE_PATH,'data')

file = 'config.ini'
CONFIG_FILE = os.path.join(BASE_PATH, 'config', file)

class Config():
   def __init__(self, file_path=CONFIG_FILE):
        '''
        定义一个配置文件的对象，默认一个文件路径，可自己补充其他路径
        :param file_path: 配置文件的绝对路径
        '''
        # 为了让写入文件的路径是唯一值，所以这样定义下来
        self.config_file_path = file_path
        # 定义配置文件对象
        self.cf = configparser.ConfigParser()
        # 读取配置文件
        self.cf.read(file_path)

   def get_key(self, section, option):
        """
        获取配置文件的value值
        :param section: 配置文件中section的值
        :param option: 配置文件中option的值
        :return value:  返回value的值
        """
        # cf对象的get方法获取value值
        value = self.cf.get(section, option)
        return value


   def set_value(self, section, option, value):
        """
        修改value的值
        :param section: 配置文件中section的值
        :param option: 配置文件中option的值
        :param value: 修改value的值
        :return: 无
        """
        # python内存先修改值
        self.cf.set(section, option, value)
        # 需要通过文件的方式写入才行，不然实体文件的值不会改变
        with open(self.config_file_path, "w+") as f:
            self.cf.write(f)


api_section='testApi'
URL = Config().get_key(api_section, 'url')  # 从config.yml读取接口地址公共字段
header = Config().get_key(api_section, 'header')  # 从config.yml读取接口地址公共字段


if __name__ == '__main__':
    print(URL)
    print(header)
