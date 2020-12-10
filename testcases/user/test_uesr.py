import re

import pytest

from api.user import User
YAML_NAME = 'user_api.yaml'

class TestUser(User):
    def setup(self):
        self.user = User()
        self.user.get_yamlname(YAML_NAME)

    def create_user_data(self):
        #add_user 为一个迭代器
        add_user= (("wu123456wu"+str(x),'测试'+str(x),"138%08d"%x)for x in range(3))
        return add_user

    @pytest.mark.parametrize('userid,name,mobile',create_user_data("xxx"))
    def test_user(self,userid,name,mobile,token):
        #创建成员验证
        data_add = {"token":token,"userid":userid,"name":name,"mobile":mobile,"department":[1]}
        # 对于添加失败的情况捕获异常，并将其删除
        try:
            assert "created" == self.user.add_user(data_add)['errmsg']
        except Exception as e:
            if 'userid existed' in e.__str__()  :
                data_del = {"token":token,"userid":userid}

            # 手机号相同但是userid不同，所以需要从返回中提取出userid
            elif 'mobile existed' in e.__str__():
                # 使用正则提取出返回值中的userid
                # 'mobile existed:xxxx'： 以：开头 '$结尾 取中间的值  (.*)
                del_userid = re.findall(":(.*)'$", e.__str__())[0]
                data_del = {"token": token, "userid": del_userid}
            self.user.del_user(data_del)
            assert "created" == self.user.add_user(data_add)['errmsg']
        #读取成员
        data_get= {"token":token,"userid":userid}
        assert name == self.user.get_user(data_get)['name']
        #更新成员 待改进
        data_update = {"userid": userid, "name": "更新"+name, "mobile": "+86 13899999999", "token": token}
        assert "updated" == self.user.update_user(data_update)['errmsg']








    def test(self,token):
        data_update = {"userid":'wu123456wu1',"name": "更新name", "mobile": "+86 13899999999","token":token}
        assert "updated"== self.user.update_user(data_update)['errmsg']

