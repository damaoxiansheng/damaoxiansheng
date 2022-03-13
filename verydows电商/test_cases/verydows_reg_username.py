'''
    结合python+selenium+unittest实现一个自动化用例。
    需求：注册的用户名的反向用例

'''
# 导包
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import  os
import sys
# 先把public做成包，只需要把当前文件的上级目录（verydows电商）加到python导包检索目录中
# 如何获取verydows电商目录
pathCurrent = os.path.abspath(os.path.dirname(__file__))
pathUp = os.path.abspath(os.path.dirname(pathCurrent))
sys.path.append(pathUp)
from public.loggingDemo import setLog,zidingyi
from public.loginlogout import login,logout

# 创建单元测试用例的类
class verydows_reg_username(unittest.TestCase):
    def setUp(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # 打开电商首页
        self.driver.get("http://39.101.167.251/qftest/")
        # 点击免费注册
        self.driver.find_element(By.LINK_TEXT,"免费注册").click()

    def test_username_01(self):
        '''用户名为空的反向测试用例'''
        # 输入用户名的反向数据
        self.driver.find_element(By.ID,"username").send_keys("")
        # 其他参数都要输入正向的数据

        # 点击立即注册按钮
        self.driver.find_element(By.LINK_TEXT,"立即注册").click()
        time.sleep(3)
        # 断言
        expectValue = "请设置用户名11"
        actualValue = self.driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[1]/dd/span/font').text
        try:
            self.assertEqual(expectValue,actualValue)
        except:
            # sl = setLog()
            # sl.setError("断言失败")
            filename = __file__.split("/")[-1]
            zidingyi(filename,self._testMethodName,expectValue,actualValue,"断言失败")

    # # 用户名为数字开头
    # def test_username_02(self):
    #     '''用户名为数字开头的反向测试用例'''
    #     # 输入用户名的反向数据
    #     self.driver.find_element(By.ID,"username").send_keys("12test")

    #     # 点击立即注册按钮
    #     self.driver.find_element(By.LINK_TEXT,"立即注册").click()
    #     time.sleep(3)
    #     # 断言
    #     expectValue = "用户名不符合格式要求"
    #     actualValue = self.driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[1]/dd/span/font').text
    #     self.assertEqual(expectValue,actualValue)

    def tearDown(self):
        # 关闭浏览器的对象
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
        