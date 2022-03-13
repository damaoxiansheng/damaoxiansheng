from selenium import webdriver
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()

driver.get("http://10.9.74.193:8088/seleniumTest/confirm.html")

anniu=driver.find_element(By.CSS_SELECTOR,"body > input[type=button]")
anniu.click()
time.sleep(2)

aa = driver.switch_to.alert

aa.accept()
time.sleep(2)
cc=aa.text
print(cc)
time.sleep(2)
aa.accept()
time.sleep(2) 
driver.quit()
