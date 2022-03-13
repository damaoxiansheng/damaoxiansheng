import unittest

import requests

session = requests.session()


class ceshi(unittest.TestCase):

    def setUp(self):
        """获取验证码"""
        a1 = session.post("http://study.qfedu.com/student/api/capchaRestController/captcha")
        self.imgAuthCodeToken = a1.json()["data"]["imgAuthCodeToken"]
        self.code = a1.json()["data"]["code"]
        # print(self.imgAuthCodeToken)
        # print(self.code)

    def test01(self):
        """登陆云学习平台"""
        a2 = session.post(url="http://study.qfedu.com/student/api/login",
                          headers={"Content-Type": "application/json"},
                          json={"mobile": "17600166826",
                                "password": "123456789",
                                "imgCode": self.code,
                                "imgToken": self.imgAuthCodeToken})
        # print(a2.json())
        global cookie
        cookie = a2.json()["data"]["token"]
        yq = "成功"
        self.assertIn(yq, a2.text)

    def test02(self):
        """点击首页"""
        a3 = session.post(url="http://study.qfedu.com/student/api/home/list",
                          headers={"Authorization": cookie})
        # print(a3.json())
        yq = "成功"
        self.assertIn(yq, a3.text)

    def test03(self):
        """点击开始学习"""
        a4 = session.post(url="http://study.qfedu.com/student/api/line/list/52",
                          headers={"Authorization": cookie})
        yq = "成功"
        self.assertIn(yq, a4.text)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
