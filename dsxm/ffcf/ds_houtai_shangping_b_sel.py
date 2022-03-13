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
        """后台商品管理商品查找用例"""
        #登录
        self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(d["username"])
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(d["password"])
        self.driver.find_element(By.XPATH,'/html/body/div/form/div/div/div[1]/a').click()
        time.sleep(10)
        yq = "常用菜单"
        sj = self.driver.find_element(By.XPATH,'//*[@id="nav"]/h2[1]').text
        self.assertEqual(yq,sj,"后台登录不成功！")
        
        #点击商品管理
        self.driver.find_element(By.XPATH,'//*[@id="nav"]/div[2]/h3/a').click()
        time.sleep(3)
        #点击商品列表
        self.driver.find_element(By.XPATH,'//*[@id="nav"]/div[2]/ul/li[1]/a').click()
        time.sleep(5)
        #切换窗口
        self.driver.switch_to.frame("main")
        #搜索框输入
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys(d["goods_name"])
        #点击搜索
        self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/button').click()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
