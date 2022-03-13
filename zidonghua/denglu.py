from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver2=webdriver.Chrome()
driver2.get("http://39.101.167.251/qftest/user/index.html")
time.sleep(1)
driver2.find_element(By.ID,"username").send_keys("asdasd")
time.sleep(1)
driver2.find_element(By.ID,"password").send_keys("123456789")
time.sleep(1)
driver2.find_element(By.NAME,"stay").click()
time.sleep(1)
driver2.find_element(By.LINK_TEXT,"登     陆").click()
time.sleep(5)