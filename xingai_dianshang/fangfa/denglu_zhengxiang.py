import json
import os
import time
import unittest

from ddt import ddt, data
from selenium import webdriver
from selenium.webdriver.common.by import By

path = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) + "\shuju\denglu_shuju.json"

with open(path, "r", encoding="utf-8") as f:
    shuju = json.load(f)


@ddt
class denglu_zhengxiang(unittest.TestCase):

    def setUp(self):
        # 打开京东网页
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.jd.com/")
        time.sleep(5)

    @data(*shuju)
    def test_01(self, d):
        # 点击登陆
        self.driver.find_element(By.LINK_TEXT, "你好，请登录").click()
        # 点击账号登陆
        self.driver.find_element(By.LINK_TEXT, "账户登录").click()
        # 输入账号
        self.driver.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(d["loginname"])
        # 输入密码
        self.driver.find_element(By.XPATH, '//*[@id="nloginpwd"]').send_keys(d["nloginpwd"])
        time.sleep(1)
        # 点击登录
        self.driver.find_element(By.XPATH, '//*[@id="loginsubmit"]').click()
        time.sleep(1)
        # 点击搜索
        self.driver.find_element(By.XPATH, '//*[@id="key"]').send_keys(d["key"])
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button/i').click()
        # 点击指定商品
        self.driver.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
