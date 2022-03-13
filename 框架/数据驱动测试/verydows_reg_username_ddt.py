'''
    数据驱动测试：
    
    结合python+selenium+unittest+ddt(data driver test)+json实现一个自动化用例。
    需求：注册的用户名的反向用例

    使用ddt模块实现数据驱动测试的步骤：
        1、安装ddt：pip3 install ddt
        2、导入ddt，from ddt import data,ddt
        3、使用@ddt修饰单元测试用例类
        4、定义一个方法来导入数据
        5、@data(*nameData)
        6、测试用例方法定义一个参数d，循环接收数据源nameData中的每一行数据，并进行参数化

'''
# 导包
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import csv
from ddt import ddt,data
import json

# 以带字典的列表
# nameDict = [
#     {"username":"","expect":"请设置用户名"},
#     {"username":"12test","expect":"用户名不符合格式要求"},
#     {"username":"test###","expect":"用户名不符合格式要求"}
# ]
def readJson():
    with open(r"框架\数据驱动测试\data.json","r",encoding="utf-8") as f:
        nameDict = json.load(f)
        return nameDict


# 创建单元测试用例的类
@ddt
class verydows_reg_username_ddt(unittest.TestCase):
    # 获取json文件返回的数据
    nameData = readJson()
    def setUp(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # 打开电商首页
        self.driver.get("http://39.101.167.251/qftest/")
        # 点击免费注册
        self.driver.find_element(By.LINK_TEXT,"免费注册").click()

    # def test_username_00(self):
    #     '''用户名为空的反向测试用例'''
    #     with open(r"./day06/data.csv","r",encoding="utf-8") as f: 
    #         data = csv.reader(f)
    #         for d in data:
    #             # 输入用户名的反向数据
    #             self.driver.find_element(By.ID,"username").clear()
    #             self.driver.find_element(By.ID,"username").send_keys(d[0])
    #             # 其他参数都要输入正向的数据

    #             # 点击立即注册按钮
    #             self.driver.find_element(By.LINK_TEXT,"立即注册").click()
    #             time.sleep(2)
    #             # 断言
    #             expectValue = d[4]
    #             actualValue = self.driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[1]/dd/span/font').text
    #             self.assertEqual(expectValue,actualValue)
    
    # @data(*nameDict):作为数据源
    @data(*nameData)
    def test_username_00(self,d):
        '''用户名为空的反向测试用例'''
        
        # 输入用户名的反向数据
        self.driver.find_element(By.ID,"username").clear()
        self.driver.find_element(By.ID,"username").send_keys(d["username"])
        # 其他参数都要输入正向的数据

        # 点击立即注册按钮
        self.driver.find_element(By.LINK_TEXT,"立即注册").click()
        time.sleep(2)
        # 断言
        expectValue = d["expect"]
        actualValue = self.driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[1]/dd/span/font').text
        self.assertEqual(expectValue,actualValue)
    def tearDown(self):
        # 关闭浏览器的对象
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
        