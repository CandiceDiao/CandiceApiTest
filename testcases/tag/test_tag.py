from api.tag import Tag
from testcases.tag.conftest import token


class TestTag(Tag):

    def test_add_tag(self,token):
        # data = self.load_yaml('tag.yaml')
        # 要把token值放入yaml文件中
        data=self.template("tag.yaml",{"token" : token,"tagname":"tn22","tagid":22},"add")
        print(self.add_tag(data))
