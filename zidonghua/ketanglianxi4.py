from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.qq.com")

driver.find_element(By.LINK_TEXT,"Qmail").click()

handles = driver.window_handles
driver.switch_to.window(handles[1])

# driver.find_element(By.LINK_TEXT,"基本版").click()
driver.switch_to.frame("login_frame")

driver.find_element(By.ID,"u").send_keys("371150995")
time.sleep(3)
driver.find_element(By.ID,"p").send_keys("1234567890")
time.sleep(3)
driver.find_element(By.ID,"login_button").click()
time.sleep(3)

driver.switch_to.parent_frame()

driver.find_element(By.LINK_TEXT,"基本版").click()
time.sleep(3)

driver.quit()
