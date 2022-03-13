import json
import os
import time
import unittest

from ddt import ddt, data
from selenium import webdriver
from selenium.webdriver.common.by import By

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + r"\sjcf\zhengxiang_denglu_gouwuche.json"
with open(path, "r", encoding="utf-8") as f:
    data1 = json.load(f)


@ddt
class ds_zxdl(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://39.101.167.251/qftest/")
        self.driver.find_element(By.LINK_TEXT, "登陆").click()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    @data(*data1)
    def test_zxdl_01(self, d):
        """正向登陆购物车验证"""
        self.driver.find_element(By.ID, "username").send_keys(d["username"])
        self.driver.find_element(By.ID, "password").send_keys(d["password"])
        self.driver.find_element(By.NAME, "stay").click()
        self.driver.find_element(By.LINK_TEXT, "登     陆").click()
        time.sleep(5)
        yq = d["dy"]
        sj = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[2]/div[1]/div[1]/h3/font[1]").text
        self.assertEqual(yq, sj)
        # 点击首页
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li/a').click()
        time.sleep(1)
        # 点击小米手机
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/ul/li[2]/div/a/img').click()
        time.sleep(1)
        # 点击加入购物车
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[4]/a[1]').click()
        time.sleep(1)
        # 点击继续购物
        self.driver.find_element(By.XPATH, '//*[@id="tocart-dialog"]/div/a[2]').click()
        time.sleep(1)
        # 继续点击首页
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li/a').click()
        time.sleep(1)
        # 点击一加手机
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[8]/div[2]/ul/li[2]/div/a/img').click()
        time.sleep(1)
        # 点击加入购物车
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[4]/a[1]').click()
        time.sleep(1)
        # 点击继续购物
        self.driver.find_element(By.XPATH, '//*[@id="tocart-dialog"]/div/a[2]').click()
        time.sleep(1)
        # 继续点击首页
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li/a').click()
        time.sleep(1)
        # 点击我的购物车
        self.driver.find_element(By.XPATH, '//*[@id="cartbar"]/font').click()
        time.sleep(1)
        time.sleep(3)
        # 点击数量添加
        self.driver.find_element(By.XPATH, '//*[@id="cart"]/div[1]/table/tbody/tr[2]/td[4]/button[2]').click()
        time.sleep(1)
        # 点击删除
        self.driver.find_element(By.XPATH, '//*[@id="cart"]/div[1]/table/tbody/tr[3]/td[6]/a').click()
        time.sleep(1)
        # 点击确定
        self.driver.find_element(By.XPATH, '//*[@id="vdspopconfirm"]/div/button[1]').click()
        time.sleep(1)
        print("11111111111111111111111111111111111111111111111111111111111111111111111111111")
        # 点击清空购物车
        self.driver.find_element(By.XPATH, '//*[@id="cart"]/div[2]/div[1]/a/i').click()
        time.sleep(1)
        print("22222222222222222222222222222222222222222222222222222222222222222222222222222")
        # 点击确定
        self.driver.find_element(By.CSS_SELECTOR, '#vdspopconfirm > div > button.sm-blue').click()
        time.sleep(1)
        print("33333333333333333333333333333333333333333333333333333333333333333333333333333")
        # 点击首页
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/a[1]').click()
        time.sleep(1)
        # 点击一加手机
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[8]/div[2]/ul/li[2]/div/a/img').click()
        time.sleep(1)
        # 点击加入购物车
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[4]/a[1]').click()
        time.sleep(1)
        # 点击继续购物
        self.driver.find_element(By.XPATH, '//*[@id="tocart-dialog"]/div/a[2]').click()
        time.sleep(1)
        # 继续点击首页
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li/a').click()
        time.sleep(1)
        # 点击我的购物车
        self.driver.find_element(By.XPATH, '//*[@id="cartbar"]/font').click()
        time.sleep(1)
        # 点击数量添加
        self.driver.find_element(By.XPATH, '//*[@id="cart"]/div[1]/table/tbody/tr[2]/td[4]/button[2]').click()
        time.sleep(1)
        # 点击去结算
        self.driver.find_element(By.XPATH, '//*[@id="checkout-btn"]').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
