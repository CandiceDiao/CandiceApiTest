'''
读取config文件
'''
import os


# os.path.abspath(__file__) 返回脚本的绝对路径
# os.path.dirname(path) 返回path父路径
# os.path.split() -》返回tuple （输出路径，文件名） 所以要去tuple[0]


BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
#将 data 文件夹拼接到输出路径下
DATA_PATH = os.path.join(BASE_PATH,'data')

file = 'config.yml'
CONFIG_FILE = os.path.join(BASE_PATH, 'config', file)

# class Config:
#     def __init__(self, config=CONFIG_FILE):
#         pass
#         # print('配置文件地址：', config)
#         # self.config = YamlReader(config).data
#
#     def get(self, element, index=0):
#         """
#         yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
#         这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
#         """
#         # return self.config[index].get(element)
#         pass
#
#
# URL = Config().get('url')  # 从config.yml读取接口地址公共字段
# header = Config().get('header')  # 从config.yml读取接口地址公共字段
# header_upload = Config().get('header_upload')  # 从config.yml读取接口地址公共字段
# # Current_Year = time.strftime("%Y", time.localtime())

if __name__ == '__main__':
    print(file)
