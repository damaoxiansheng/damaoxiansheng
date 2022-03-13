import time
import unittest
import selenium
from appium import webdriver
from selenium.webdriver.common.by import By
import json
import fangfa
from ddt import ddt,data
import os

path = os.path.dirname(__file__) + "/data.json"

with open(path,"r",encoding="utf-8") as f:
    a = json.load(f)

@ddt
class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.tencent.mobileqq'
        desired_caps["noReset"] = True
        desired_caps['appActivity'] = 'com.tencent.mobileqq.activity.LoginActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.dd = fangfa.fangfa(self.driver)

    @data(*a)
    def test_01(self,d):
        time.sleep(5)
        self.dd.dianji("id","com.tencent.mobileqq:id/btn_login")
        time.sleep(8)
        self.dd.shuru("xpath","//android.widget.EditText[@content-desc='请输入QQ号码或手机或邮箱']",d["zhanghao"])
        time.sleep(3)
        self.dd.shuru("xpath","//android.widget.EditText[@content-desc='密码 安全']",d["mima"])
        time.sleep(3)
        self.dd.dianji("id","com.tencent.mobileqq:id/login")
        time.sleep(10)
        yq = "babyQ"
        sj = self.driver.find_element(By.ID,'com.tencent.mobileqq:id/ok4').text
        self.assertEqual(yq,sj,"用例执行不成功！！！")
        self.driver.swipe(144,1084,922,1084,1000)
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    time.sleep(8)
