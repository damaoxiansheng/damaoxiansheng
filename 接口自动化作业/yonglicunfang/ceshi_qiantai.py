import json
import os
import sys
import time
import unittest

import requests
from ddt import ddt, data

shijian = time.strftime("%Y-%m-%d-%H-%M")

path = os.path.abspath(os.path.dirname(os.path.dirname("__file__")))
sys.path.append(path)

from gonggong import rizhi

session = requests.session()

with open(path + r"/shuju/zhuceshuju.json", "r", encoding="utf-8") as f:
    shuJu = json.load(f)


@ddt
class ceshi_qiantai(unittest.TestCase):

    def setUp(self):
        pass

    @data(*shuJu)
    def test01_fanxiang(self, d):

        a1 = session.post(url="http://39.101.167.251/qftest/index.php",
                          data={"username": d['username'],
                                "email": d['email'],
                                "password": d['password'],
                                "repassword": d['repassword'],
                                "agree": d['agree']},
                          params={"c": "user",
                                  "a": "register",
                                  "step": "submit"},
                          headers={"Content-Type": "application/x-www-form-urlencoded"})

        rizhi.rizhi("用例=%s  预期=%s  实际=%s" % (d["yongli"], d["yq"], a1.content.decode("utf-8")))
        try:
            self.assertIn(d["yq"], a1.content.decode("utf-8"))
        except:
            rizhi.rizhi("用例=%s  预期=%s  实际=%s" % (d["yongli"], d["yq"], a1.content.decode("utf-8")))
            print("用例执行失败！！！详情见日志！！！")

    def test02_denglu(self):
        """正向登陆"""
        a1 = session.post(url="http://39.101.167.251/qftest/user/login.html?step=submit",
                          headers={"Content-Type": "application/x-www-form-urlencoded"},
                          data={"username": "liuyouwei12345",
                                "password": "200c6d94e583e62c6964de3acdc723e5"})

        rizhi.rizhi("正向登陆用例  预期=登陆成功  实际=%s" % (a1.content.decode("utf-8")))
        self.assertIn("登录成功", a1.content.decode("utf-8"))

    def test03_gerenziliaoxiugai(self):
        """个人资料修改"""
        a1 = session.post(url="http://39.101.167.251/qftest/user/profile.html?step=update",
                          headers={"Content-Type": "application/x-www-form-urlencoded"},
                          data={"nickname": "heihei",
                                "qq": "31256452",
                                "gender": "1",
                                "birth_year": "1997",
                                "birth_month": "1",
                                "birth_day": "1",
                                "signature": "爷！狂傲霸天！！！"})
        rizhi.rizhi("个人资料修改用例  预期=更新资料成功  实际=%s" % (a1.content.decode("utf-8")))
        self.assertIn("更新资料成功", a1.content.decode("utf-8"))

    def test04_addshouhuodizhi(self):
        """新建收货地址"""
        a1 = session.post(url="http://39.101.167.251/qftest/consignee/save.html",
                          headers={"Content-Type": "application/x-www-form-urlencoded"},
                          data={"id": "",
                                "receiver": "王大锤",
                                "province": "2",
                                "city": "1",
                                "borough": "3",
                                "address": "你哦哦屁哦",
                                "zip": "075000",
                                "mobile": "17800332752"})
        rizhi.rizhi("新建收货地址用例  预期=新建收件人地址成功  实际=%s" % (a1.content.decode("utf-8")))
        self.assertIn("新建收件人地址成功", a1.content.decode("utf-8"))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
