import os


# os.path.abspath(__file__) 返回脚本的绝对路径
# os.path.dirname(path) 返回path父路径
# os.path.split() -》返回tuple （输出路径，文件名） 所以要去tuple[0]
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
#将 data 文件夹拼接到输出路径下
DATA_PATH = os.path.join(BASE_PATH, 'data')

