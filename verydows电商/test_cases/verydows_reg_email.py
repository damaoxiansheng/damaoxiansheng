'''
    结合python+selenium+unittest实现一个自动化用例。
    需求：注册的邮箱的反向用例

'''
# 导包
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

# 创建单元测试用例的类
class verydows_reg_email(unittest.TestCase):
    def setUp(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # 打开电商首页
        self.driver.get("http://39.101.167.251/qftest/")
        # 点击免费注册
        self.driver.find_element(By.LINK_TEXT,"免费注册").click()

    def test_email_01(self):
        '''邮箱为空的反向测试用例'''
        # 输入邮箱的反向数据
        self.driver.find_element(By.ID,"email").send_keys("")
        # 其他参数都要输入正向的数据
        
        # 点击立即注册按钮
        self.driver.find_element(By.LINK_TEXT,"立即注册").click()
        time.sleep(3)
        # 断言
        expectValue = "请设置邮箱"
        actualValue = self.driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[2]/dd/span/font').text
        self.assertEqual(expectValue,actualValue)

    # 用户名为数字开头
    def test_email_02(self):
        '''邮箱为缺少@和域名的反向测试用例'''
        # 输入邮箱的反向数据（缺少@和域名）
        self.driver.find_element(By.ID,"email").send_keys("12test")

        # 点击立即注册按钮
        self.driver.find_element(By.LINK_TEXT,"立即注册").click()
        time.sleep(3)
        # 断言
        expectValue = "无效的邮箱地址"
        actualValue = self.driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[2]/dd/span/font').text
        self.assertEqual(expectValue,actualValue)

    def tearDown(self):
        # 关闭浏览器的对象
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
        