"""
成员管理
"""
from api.base_api import BaseApi


class User(BaseApi):

    def get_yamlname(self,yamlname):
        self.yamlname = yamlname

    def add_user(self,data):
        data=self.template(self.yamlname,data,"add")
        return self.send_api(data).json()

    def del_user(self,data):
        data = self.template(self.yamlname, data, "delete")
        return self.send_api(data).json()

    def get_user(self,data):
        data = self.template(self.yamlname, data, "get")
        return self.send_api(data).json()

    def update_user(self,update_data:dict):
        data =self.template(self.yamlname, {"token":update_data['token']}, "update")
        for key,value in update_data.items():
            data["json"][key] = value
        return self.send_api(data).json()
