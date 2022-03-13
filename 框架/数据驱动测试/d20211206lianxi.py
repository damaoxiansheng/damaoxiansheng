import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import json
from ddt import ddt,data

with open(r"框架\数据驱动测试\data.json","r",encoding="utf-8") as f:
    a = json.load(f)
    print(a)
@ddt
class lianxi(unittest.TestCase):
    
    def setUp(self):
        #创建对象打开浏览器
        self.driver = webdriver.Chrome()
        #对象打开浏览器网址
        self.driver.get("http://39.101.167.251/qftest/")
        #点击免费注册
        self.driver.find_element(By.LINK_TEXT,"免费注册").click()
        time.sleep(2)
    
    @data(*a)
    def test_01(self,d):
        #清除输入框数据
        self.driver.find_element(By.ID,"username").clear()
        #输入用户名
        self.driver.find_element(By.ID,"username").send_keys(d["username"])
        time.sleep(1)
        
        #输入邮箱
        self.driver.find_element(By.ID,"email").clear()
        self.driver.find_element(By.ID,"email").send_keys(d["yx"])
        time.sleep(1)
        
        #输入密码
        self.driver.find_element(By.ID,"password").clear()
        self.driver.find_element(By.ID,"password").send_keys(d["mm"])
        time.sleep(1)
        
        #再次输入密码
        self.driver.find_element(By.ID,"repassword").clear()
        self.driver.find_element(By.ID,"repassword").send_keys(d["qemm"])
        time.sleep(1)
        
        #点击立即注册
        self.driver.find_element(By.LINK_TEXT,"立即注册").click()
        time.sleep(1)
        
        yq = d["expect"]
        sj = self.driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[1]/dd/span/font').text
        self.assertEqual(yq,sj)
        
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()