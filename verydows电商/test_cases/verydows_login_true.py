'''
    正常登录的用例：
        电商首页，点击登录
        登录页面输入用户名、密码
        点击登录

        断言：
            登录后的用户名作为断言

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import  time
import unittest
# 还希望日志功能（在public下）
import  os
import sys
# 先把public做成包，只需要把当前文件的上级目录（verydows电商）加到python导包检索目录中
# 如何获取verydows电商目录
pathCurrent = os.path.abspath(os.path.dirname(__file__))
pathUp = os.path.abspath(os.path.dirname(pathCurrent))
sys.path.append(pathUp)
from public.loggingDemo import setLog,zidingyi

# 创建单元测试类
class verydows_login_true(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 最大化
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(10)
        self.driver.get("http://39.101.167.251/qftest/")

    def test_login_01(self):
        # 点击首页的登录按钮
        self.driver.find_element(By.LINK_TEXT,"登陆").click()
        #输入用户名
        self.driver.find_element(By.ID,"username").send_keys("bk2104_001")
        self.driver.find_element(By.ID,"password").send_keys("123456")

        # 点击登陆按钮
        self.driver.find_element(By.LINK_TEXT,"登     陆").click()
        time.sleep(5)
        # 断言
        try:
            expectValue = "bk2104_002"
            acutalValue = self.driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[1]/div[1]/h3/font[1]').text
            self.assertEqual(expectValue,acutalValue)
        except:
            filename = __file__.split("/")[-1]
            zidingyi(filename,self._testMethodName,expectValue,acutalValue,"测试执行失败")

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()