from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from ddt import ddt,data
import os
import json

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + r"\sjcf\zhengxiang_denglu_gerenzhongxin.json"
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
        """正向登陆,个人中心咨询反馈"""
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
        #点击咨询反馈
        self.driver.find_element(By.XPATH,'//*[@id="usermenu"]/li[8]/a').click()
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/a').click()
        print("?????????????????????????????????????????????????????????????????????????????????")
        #主题输入内容
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div/form/div/div/table/tbody/tr[1]/td/input').send_keys(d["zxfk_zt"])
        #点击类型
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div/form/div/div/table/tbody/tr[2]/td/div/label[4]/input').click()
        #详细内容输入
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div/form/div/div/table/tbody/tr[3]/td/textarea').send_keys(d["zxfk_xxnr"])
        #输入手机号
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div/form/div/div/table/tbody/tr[4]/td/input').send_keys(d["zxfk_sjh"])
        #点击确定提交
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div/form/div/div/table/tbody/tr[5]/td/div/button').click()
        #断言
        yq4 = d["dy4"]
        sj4 = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/h3").text
        self.assertEqual(yq4,sj4,"提交不成功！")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()