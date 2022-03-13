import os
import sys
import time
import unittest

import requests

shijian = time.strftime("%Y-%m-%d-%H-%M")

path = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname("__file__"))))
sys.path.append(path)

from gonggong import rizhi

session = requests.session()

class yunxuexi(unittest.TestCase):

    def setUp(self):
        # 初始化拿到登陆用的imgCode和imgToken
        a1 = session.post(url="http://study.qfedu.com/student/api/capchaRestController/captcha")
        self.token = a1.json()["data"]["imgAuthCodeToken"]
        self.code = a1.json()["data"]["code"]

    def test01(self):
        """登陆用例"""
        a2 = session.post(url="http://study.qfedu.com/student/api/login",
                          headers={"Content-Type": "application/json"},
                          json={"mobile": "17600166826",
                                "password": "123456789",
                                "imgCode": self.code,
                                "imgToken": self.token})
        rizhi.rizhi("test01登陆用例  预期=" + "成功  ""实际=" + a2.text)
        global token
        token = a2.json()["data"]["token"]
        self.assertIn("成功", a2.text)

    def test02(self):
        """点击开始学习"""
        a3 = session.post(url="http://study.qfedu.com/student/api/line/list/52",
                          headers={"Authorization": token})
        rizhi.rizhi("test02点击开始学习用例  预期=" + "软件测试快速入门技术  ""实际=" + a3.text)
        self.assertIn("软件测试快速入门技术", a3.text)

    def test03(self):
        """进去开始学习后点击一门课程开始学习"""
        a4 = session.post(url="http://study.qfedu.com/student/api/line/stageList/50",
                          headers={"Authorization": token})
        rizhi.rizhi("test03点击开始学习用例  预期=" + "Web系统需求分析  ""实际=" + a4.text)
        self.assertIn("Web系统需求分析", a4.text)

    def test04(self):
        """学习课程：Web系统需求分析视频"""
        a5 = session.post(url="http://study.qfedu.com/student/api/line/info/606",
                          headers={"Authorization": token})
        rizhi.rizhi("test04学习课程用例  预期=" + "SC01-web系统需求分析1  ""实际=" + a5.text)
        self.assertIn("SC01-web系统需求分析1", a5.text)

    def test05(self):
        """点击在线刷题"""
        a6 = session.post(url="http://study.qfedu.com/student/api/question/label/list",
                          headers={"Authorization": token})
        rizhi.rizhi("test05点击在线刷题用例  预期=" + "预习阶段  ""实际=" + a6.text)
        self.assertIn("预习阶段", a6.text)

    def test06(self):
        """点击个人中心"""
        a7 = session.post(url="http://study.qfedu.com/student/api/personal/center/info",
                          headers={"Authorization": token})
        rizhi.rizhi("test06点击个人中心  预期=" + "成功  ""实际=" + a7.text)
        self.assertIn("成功", a7.text)

    def test07(self):
        """个人中心修改头像"""
        a8 = session.post(url="http://study.qfedu.com/student/api/personal/center/modifyAvatar",
                          headers={"Authorization": token,
                                   "Content-Type": "application/json"},
                          json={"imgUrl": "http://qfyx.bj.bcebos.com/img/students/2022-01-05/20220105194342.jpg"})
        rizhi.rizhi("test07个人中心修改头像用例  预期=" + "成功  ""实际=" + a8.text)
        self.assertIn("成功", a8.text)

    def test08(self):
        """个人信息修改"""
        a9 = session.post(url="http://study.qfedu.com/student/api/personal/center/updateSutdentInfo",
                          headers={"Authorization": token},
                          json={"email": "371150995@qq.com",
                                "gender": 1,
                                "id": 133,
                                "nickName": "无敌暴龙11111",
                                "personalSignature": "",
                                "qq": 371150998,
                                "userName": "刘有韦"})
        rizhi.rizhi("test08个人信息修改用例  预期=" + "成功  ""实际=" + a9.text)
        self.assertIn("成功", a9.text)

    def test09(self):
        """意见反馈提交测试"""
        a10 = session.post(url="http://study.qfedu.com/student/api/personal/center/saveSuggestions",
                           headers={"Authorization": token},
                           json={"type": 1,
                                 "content": "我靠！棒棒棒，哈哈哈哈哈哈",
                                 "suggestionsAttachList": []})
        rizhi.rizhi("test09意见反馈提交测试用例  预期=" + "成功  ""实际=" + a10.text)
        self.assertIn("成功", a10.text)

    def test10(self):
        """错误密码登陆"""
        a11 = session.post(url="http://study.qfedu.com/student/api/login",
                           json={"mobile": "17600166826",
                                 "password": "1234567891",
                                 "imgCode": "85067",
                                 "imgToken": "baf30dad-8e01-4441-9667-c6887bf56696"})
        rizhi.rizhi("test10错误密码登陆用例  预期=" + "密码输入错误  ""实际=" + a11.text)
        self.assertIn("密码输入错误", a11.text)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
