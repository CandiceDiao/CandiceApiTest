import pytest

from api.tag import Tag
from testcases.tag.conftest import token


class TestTag(Tag):

    tag =Tag()
    data = tag.load_yaml('tag_data.yaml')
    tag_add = data['add']

    @pytest.mark.parametrize('tagid,tagname',tag_add)
    def test_add_tag(self,token,tagid,tagname):
        print(self.add_tag(token,tagid,tagname))




