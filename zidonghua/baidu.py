import time
from selenium import webdriver
driver = webdriver.Chrome()
time.sleep(1)
driver.get("https://www.baidu.com/")
time.sleep(1)
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(1)
driver.find_element_by_id("su").click()
time.sleep(2)
driver.quit()