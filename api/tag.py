"""
标签管理
"""
from api.base_api import BaseApi

API_YAML='tag_api.yaml'

class Tag(BaseApi):


    def add_tag(self,token,tagid,tagname):
        data={"token":token,"tagid":tagid,"tagname":tagname}
        data = self.template(API_YAML, data, "add")
        return self.send_api(data).json()





