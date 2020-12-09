"""
获取token
"""
import pytest

from api.base_api import BaseApi


class Token(BaseApi):

    def get_token(self,data):
        res=self.send_api(data)
        try:
            return res.json()['access_token']
        except Exception as e:
            raise ValueError("requests token error")




