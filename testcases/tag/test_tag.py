import pytest


from api.tag import Tag
from utils.config import URL
from utils.file_reader import YamlReader


class TestTag(Tag):
    tag =Tag()
    #读取出yaml文件中的数据，数据类型为dict
    data = YamlReader('tag_data.yaml').load_yaml()
    #在读取的数据中找到key为add的数据，值类型为list
    tag_add = data['add']['data']
    tag_ids = data['add']['ids']

    # 使用参数化，数据都保存在yml文件，读取出来变成tag_add
    @pytest.mark.parametrize('tagid,tagname',tag_add, ids=tag_ids)
    def test_add_tag(self,token,tagid,tagname):
        self.tag.set_session({"access_token": token})
        data = {"url":URL,tagid:"tagid",tagname:"tagname"}
        print(self.tag.add_tag(data))




