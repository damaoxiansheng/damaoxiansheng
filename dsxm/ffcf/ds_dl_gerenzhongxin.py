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
        """正向登陆,个人中心验证"""
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
        #点击上传头像
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="avatar-form"]/input[1]').send_keys(r"D:\pythonzuoye\dsxm\ggmk\tupian.png")
        #点击保存头像
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="save-avatar-btn"]').click()
        #昵称输入
        self.driver.find_element(By.XPATH,'//*[@id="nickname"]').clear()
        self.driver.find_element(By.XPATH,'//*[@id="nickname"]').send_keys(d["gxmz"])
        #输入qq
        self.driver.find_element(By.XPATH,'//*[@id="qq"]').clear()
        self.driver.find_element(By.XPATH,'//*[@id="qq"]').send_keys(d["qq"])
        #指定性别
        self.driver.find_element(By.CSS_SELECTOR,'#profile-form > dl:nth-child(3) > dd > label:nth-child(2) > input[type=radio]').click()
        #指定年
        self.driver.find_element(By.XPATH,'//*[@id="birth_year"]/option[77]').click()
        #指定月
        self.driver.find_element(By.XPATH,'//*[@id="birth_month"]/option[8]').click()
        #指定日
        self.driver.find_element(By.XPATH,'//*[@id="birth_day"]/option[23]').click()
        #编辑个性签名
        self.driver.find_element(By.XPATH,'//*[@id="signature"]').clear()
        self.driver.find_element(By.XPATH,'//*[@id="signature"]').send_keys(d["gxqm"])
        #点击更新资料
        self.driver.find_element(By.XPATH,'//*[@id="profile-form"]/div/button').click()
        #添加断言
        yq2 = d["dy2"]
        sj2 = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/h3').text
        self.assertEqual(yq2,sj2,"资料更不成功")
        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()