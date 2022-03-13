from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest  
import time
from ddt import ddt,data
import os
import json

path = os.path.abspath(os.path.dirname( os.path.dirname(__file__))) + r"\sjcf\zhengxiang_denglu_gerenzhongxin.json"
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
    
    @data(*data1)    
    def test_zxdl_01(self,d):
        """正向登陆,收件地址"""
        self.driver.find_element(By.ID,"username").send_keys(d["username"])
        self.driver.find_element(By.ID,"password").send_keys(d["password"])
        self.driver.find_element(By.NAME,"stay").click()
        self.driver.find_element(By.LINK_TEXT,"登     陆").click()
        time.sleep(5)
        yq = d["dy"]
        sj = self.driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[2]/div[1]/div[1]/h3/font[1]").text
        self.assertEqual(yq,sj)
        #点击个人中心
        self.driver.find_element(By.LINK_TEXT,"编辑").click()
        #点击收件地址
        self.driver.find_element(By.LINK_TEXT,'收件地址').click()
        #点击新建收件人
        self.driver.find_element(By.XPATH,'//*[@id="newadrbtn"]').click()
        #选择收件人
        self.driver.find_element(By.XPATH,'//*[@id="receiver"]').send_keys(d["sjr"])
        #选择省份
        self.driver.find_element(By.XPATH,'//*[@id="areaslt-province"]/option[4]').click()
        #选择城市
        self.driver.find_element(By.XPATH,'//*[@id="areaslt-city"]/option[8]').click()
        #选择区/县
        self.driver.find_element(By.XPATH,'//*[@id="areaslt-borough"]/option[7]').click()
        #详细地址
        self.driver.find_element(By.XPATH,'//*[@id="address"]').send_keys(d["xxdz"])
        #输入邮编
        self.driver.find_element(By.XPATH,'//*[@id="zip"]').send_keys(d["yb"])
        #输入手机号码//*[@id="mobile"]
        self.driver.find_element(By.XPATH,'//*[@id="mobile"]').send_keys(d["sjhm"])
        #点击保存信息
        self.driver.find_element(By.XPATH,'//*[@id="consignee-form"]/div/div/button[1]').click()
        # #断言/html/body/div/div[2]/h3
        # yq3 = d["dy3"]
        # sj3 = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/h3").text
        # self.assertEqual(yq3,sj3,"不成功")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()