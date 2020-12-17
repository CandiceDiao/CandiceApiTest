import re

import allure
import pytest


from api.user import User
from utils.config import URL

YAML_NAME = 'user_api.yaml'

@allure.feature("通讯录模块")
class TestUser(User):
    def setup(self):
        self.user = User()
        self.user.get_yamlname(YAML_NAME)


    def create_user_data(self):
        #add_user 为一个迭代器
        add_user= (("wu123456wu"+str(x),'测试'+str(x),"138%08d"%x)for x in range(3))
        return add_user

    @allure.story("整体流程")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('userid,name,mobile',create_user_data("xxx"),
                             ids=['用户1','用户2','用户3'])

    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    def test__all_user(self,userid,name,mobile,token):
        # 将token保存到Session()中
        self.user.set_session({"access_token": token})
        #创建成员验证
        data_add = {"url":URL,"userid":userid,"name":name,"mobile":mobile,"department":[1]}
        # 对于添加失败的情况捕获异常，并将其删除
        try:
            with allure.step("添加成员"):
                assert "created" == self.user.add_user(data_add)['errmsg']
        except Exception as e:
            if 'userid existed' in e.__str__()  :
                data_del = {"url":URL,"userid": userid}

            # 手机号相同但是userid不同，所以需要从返回中提取出userid
            elif 'mobile existed' in e.__str__():
                # 使用正则提取出返回值中的userid
                # 'mobile existed:xxxx'： 以：开头 '$结尾 取中间的值  (.*)
                #【待解决问题】并发是正则取不到值
                del_userid = re.findall(":(.*)'$", e.__str__())[0]
                data_del = {"url":URL,"userid": del_userid}
            with allure.step("删除已存在的成员"):
                self.user.del_user(data_del)
            assert "created" == self.user.add_user(data_add)['errmsg']
        #读取成员
        with allure.step("读取成员"):
            data_get= {"url":URL,"userid":userid}
            assert name == self.user.get_user(data_get)['name']
        data_del = {"url": URL, "userid": userid}
        self.user.del_user(data_del)
        # #更新成员 待改进
        # data_update = {"userid": userid, "name": "更新"+name, "mobile": "+86 13899999999", "token": token}
        # assert "updated" == self.user.update_user(data_update)['errmsg']

    @allure.story("添加通讯录冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize('userid,name,mobile',[("s1","smokeuser","13899999999")],ids=["添加通讯录冒烟测试"])
    def test_add_user(self,userid,name,mobile,token):
        self.user.set_session({"access_token": token})
        add_user={"url":URL,"userid":userid,"name":name,"mobile":mobile,"department":[1]}
        assert "created"== self.user.add_user(add_user)['errmsg']
        del_user = {"url":URL,"userid":userid}
        self.user.del_user(del_user)



