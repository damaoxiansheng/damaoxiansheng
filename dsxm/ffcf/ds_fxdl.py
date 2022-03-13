from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest  
import time
from ddt import ddt,data
import os
import json

path = os.path.abspath(os.path.dirname( os.path.dirname(__file__))) + r"\sjcf\fanxiang_denglusj.json"
with open(path,"r",encoding="utf-8") as f:
    data1 = json.load(f)

@ddt
class ds_zxdl(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://39.101.167.251/qftest/")
        self.driver.find_element(By.LINK_TEXT,"登陆").click()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        
    # @data(*data1)   
    # def test_zxdl_01(self,d):
    #     """正向登陆"""
    #     self.driver.find_element(By.ID,"username").send_keys(d["zxyhm"])
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"password").send_keys(d["zxmm"])
    #     time.sleep(1)
    #     self.driver.find_element(By.NAME,"stay").click()
    #     time.sleep(1)
    #     self.driver.find_element(By.LINK_TEXT,"登     陆").click()
    #     time.sleep(5)
    #     yq = d["zxdy"]
    #     sj = self.driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[2]/div[1]/div[1]/h3/font[1]").text
    #     self.assertEqual(yq,sj)
        
    # def test_fxdl_01(self):
    #     """反向空用户名登陆"""
    #     self.driver.find_element(By.ID,"username").send_keys("")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"password").send_keys("123456789")
    #     time.sleep(1)
    #     self.driver.find_element(By.NAME,"stay").click()
    #     time.sleep(1)
    #     self.driver.find_element(By.LINK_TEXT,"登     陆").click()
    #     yq = "请输入用户名"
    #     sj = self.driver.find_element(By.XPATH,'//*[@id="login-form"]/div/dl[1]/dd/span/font').text
    #     self.assertEqual(yq,sj)
    @data(*data1)
    def test_fxdl_02(self,d):
        """反向错误账号或者密码登陆"""
        self.driver.find_element(By.ID,"username").send_keys(d["username"])
        time.sleep(1)
        self.driver.find_element(By.ID,"password").send_keys(d["password"])
        time.sleep(1)
        self.driver.find_element(By.NAME,"stay").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT,"登     陆").click()
        yq = d["dy"]
        sj = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/h3').text
        self.assertEqual(yq,sj)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()