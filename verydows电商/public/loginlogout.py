# 导包
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
def login(driver):
    # 1、打开电商首页
    driver.get("http://39.101.167.251/qftest/")
    # 2、点击登陆
    driver.find_element(By.LINK_TEXT,'登陆').click()
    # 3、输入用户名
    driver.find_element(By.NAME,"username").send_keys("bk2104_001")
    # 4、输入密码
    driver.find_element(By.NAME,"password").send_keys("123456")
    # 5、登陆
    driver.find_element(By.LINK_TEXT,'登     陆').click()
    # 5s的等待
    time.sleep(5)

def logout(driver):
    # 6、退出（修改个人中心、增加购物车等）
    ele = driver.find_element(By.XPATH,'//*[@id="top-userbar"]/a')
    ActionChains(driver).move_to_element(ele).perform()
    driver.find_element(By.LINK_TEXT,"退出").click()
    time.sleep(3)

