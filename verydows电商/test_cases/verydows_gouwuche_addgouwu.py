'''
    登录后，商品加入购物车。
        登录账号（模块）
        点击首页
        点击一个商品
        在商品详情页点击加入购物车
        立即结算
        跳转到购物车页面
        断言：商品数大于0就添加成功。
        点击退出登录（模块）

'''
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import  time
import unittest
# 还希望日志功能（在public下）
import  os
import sys
# 先把public做成包，只需要把当前文件的上级目录（verydows电商）加到python导包检索目录中
# 如何获取verydows电商目录
pathCurrent = os.path.abspath(os.path.dirname(__file__))
pathUp = os.path.abspath(os.path.dirname(pathCurrent))
sys.path.append(pathUp)
from public.loggingDemo import setLog,zidingyi
from public.loginlogout import login,logout

class verydows_gouwuche_addgouwu(unittest.TestCase):
    def setUp(self):
        self.driver =  webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # 登录
        login(self.driver)

    def test_gouwuche_01(self):
        # 点击首页
        self.driver.find_element(By.LINK_TEXT,"首页").click()
        # 点击一个商品
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/ul/li[1]/h3/a').click()
        # 在商品详情页点击加入购物车
        self.driver.find_element(By.LINK_TEXT,"加入购物车").click()
        # 结算付款
        self.driver.find_element(By.LINK_TEXT,"结算付款").click()
        # 跳转到购物车页面
        # 断言：商品数大于0就添加成功，count用来获取购物车中实际数量
        count=0
        try:
            # 来获取购物车中实际数量
            count = int(self.driver.find_element(By.XPATH,'//*[@id="item-count"]').text)
            # 商品数大于0就添加成功
            self.assertTrue(count>0)
        except:
            filename = __file__.split("/")[-1]
            zidingyi(filename,self._testMethodName,count,"测试执行失败")

        def tearDown(self):
            # 退出登录
            logout(self.driver)
            # 关闭浏览器
            self.driver.quit()   

if __name__=="__main__":
    unittest.main()