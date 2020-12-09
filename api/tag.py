"""
标签管理
"""
from api.base_api import BaseApi


class Tag(BaseApi):



    def add_tag(self,data):

        return self.send_api(data).json()

