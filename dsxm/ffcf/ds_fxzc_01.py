from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest  
import time
from ddt import ddt,data
import os
import json

path = os.path.abspath(os.path.dirname( os.path.dirname(__file__))) + r"\sjcf\fanxiang_zhuce.json"
with open(path,"r",encoding="utf-8") as f:
    data1 = json.load(f)
    
@ddt
class ds_zxdl(unittest.TestCase):
    
    def setUp(self):
        #创建对象
        self.driver = webdriver.Chrome()
        #对象打开浏览器网址
        self.driver.get("http://39.101.167.251/qftest/")
        #点击免费注册
        self.driver.find_element(By.LINK_TEXT,"免费注册").click()
        #延时1秒
        time.sleep(1)
    
    @data(*data1)    
    def test_zxdl_01(self,d):
        """反向注册案例：为空、4位字符、17位字符、数字用户名、特殊符号用户名"""
        #输入用户名
        self.driver.find_element(By.ID,"username").clear()
        self.driver.find_element(By.ID,"username").send_keys(d["username"])
        #输入邮箱
        self.driver.find_element(By.ID,"email").clear()
        self.driver.find_element(By.ID,"email").send_keys(d["email"])

        #输入密码
        self.driver.find_element(By.ID,"password").clear()
        self.driver.find_element(By.ID,"password").send_keys(d["password"])
        
        #再次输入密码
        self.driver.find_element(By.ID,"repassword").clear()
        self.driver.find_element(By.ID,"repassword").send_keys(d["repassword"])
        
        #点击立即注册
        self.driver.find_element(By.LINK_TEXT,"立即注册").click()
        time.sleep(1)
        
        #断言
        yq = d["dy"]
        sj = self.driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[1]/dd/span/font').text
        self.assertEqual(yq,sj)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()