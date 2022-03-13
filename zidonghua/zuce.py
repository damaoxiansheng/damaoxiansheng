"""
    注册页面邮箱为空用例设计
"""
#导包
from selenium import webdriver
import time
from fangfa import dl
driver = webdriver.Chrome()
a = "aspmnkaq"
b = "6ammq8@qq.com"
c =  "123456"
d = "123456"
dl(driver,a,b,c,d)
print("=====================================================")
time.sleep(5)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
driver.quit()
print("????????????????????????????????????????????????????")
# #设置断言
# yuqi = "请设置邮箱"
# shiji = driver.find_element(By.CSS_SELECTOR,"#register-form > div > dl:nth-child(2) > dd > span > font").text
# if yuqi == shiji:
#     print("用例执行成功！！！！！！！！！")
# else:
#     print("用例执行失败！！！！！！！！")
    
#关闭浏览器
# driver.quit()