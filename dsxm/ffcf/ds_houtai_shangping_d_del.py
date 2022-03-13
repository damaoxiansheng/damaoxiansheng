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
        """后台商品管理商品删除用例"""
        #登录
        self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(d["username"])
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(d["password"])
        self.driver.find_element(By.XPATH,'/html/body/div/form/div/div/div[1]/a').click()
        yq = "常用菜单"
        sj = self.driver.find_element(By.XPATH,'//*[@id="nav"]/h2[1]').text
        self.assertEqual(yq,sj,"后台登录不成功！")
        
        #点击商品管理
        self.driver.find_element(By.XPATH,'//*[@id="nav"]/div[2]/h3/a').click()
        #点击商品列表
        self.driver.find_element(By.XPATH,'//*[@id="nav"]/div[2]/ul/li[1]/a').click()
        #切换窗口
        self.driver.switch_to.frame("main")
        #点击勾选商品
        self.driver.find_element(By.XPATH,'//*[@id="rows"]/table/tbody/tr[2]/td[1]/input').click()
        time.sleep(2)
        #点击删除商品
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/a[6]/font').click()
        time.sleep(2)
        #添加断言
        yq1 = "删除商品成功"
        sj1 = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/h3').text
        self.assertEqual(yq1,sj1,"删除商品不成功")
        time.sleep(3)
        
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
