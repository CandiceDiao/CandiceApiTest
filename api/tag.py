"""
标签管理
"""
from api.base_api import BaseApi
from utils.file_reader import YamlReader

API_YAML='tag_api.yaml'
from utils.config import DATA_PATH

class Tag(BaseApi):


    def add_tag(self,data):
        data = YamlReader(API_YAML).template(data, "add")
        return self.send_api(data).json()





