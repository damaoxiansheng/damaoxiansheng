import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import json
from ddt import ddt,data 

path = os.path.abspath(os.path.dirname(__file__))
path1 = os.path.abspath(os.path.dirname(path)) + r"\sjcf\ds_houduan_dl.json"
with open(path1,"r",encoding="utf-8") as f:
    data1 = json.load(f)

@ddt
class ds_houduan_dl(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://39.101.167.251/qftest/index.php?m=backend")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    
    @data(*data1)    
    def test_dl_01(self,d):
        """后台登陆用例"""
        self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(d["username"])
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(d["password"])
        self.driver.find_element(By.XPATH,'/html/body/div/form/div/div/div[1]/a').click()
        time.sleep(10)
        yq = "常用菜单"
        sj = self.driver.find_element(By.XPATH,'//*[@id="nav"]/h2[1]').text
        self.assertEqual(yq,sj,"后台登录不成功！")
    
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
