from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

#创建对象
driver = webdriver.Chrome()
#对象打开浏览器网址
driver.get("http://39.101.167.251/qftest/")
#点击免费注册
driver.find_element(By.LINK_TEXT,"免费注册").click()
#延时1秒
time.sleep(1)

#正向注册
def zxzc():
    with open(r"zidonghua\zxzc.csv","r",encoding="utf-8") as f:
        a1=csv.reader(f)
        for i in a1:
            print(i)
            #输入用户名
            driver.find_element(By.ID,"username").clear()
            driver.find_element(By.ID,"username").send_keys(i[0])
            #输入邮箱
            driver.find_element(By.ID,"email").clear()
            driver.find_element(By.ID,"email").send_keys(i[1])

            #输入密码
            driver.find_element(By.ID,"password").clear()
            driver.find_element(By.ID,"password").send_keys(i[2])
           
            #再次输入密码
            driver.find_element(By.ID,"repassword").clear()
            driver.find_element(By.ID,"repassword").send_keys(i[3])
            
            #点击立即注册
            driver.find_element(By.LINK_TEXT,"立即注册").click()
            time.sleep(5)
            driver.quit()
            
#反向注册———>用户名
def fxzc():
    #创建对象
    driver = webdriver.Chrome()
    #对象打开浏览器网址
    driver.get("http://39.101.167.251/qftest/")
    #点击免费注册
    driver.find_element(By.LINK_TEXT,"免费注册").click()
    #延时1秒
    time.sleep(1)
    with open(r"zidonghua\fxzc.csv","r",encoding="utf-8") as f:
        a1=csv.reader(f)
        for i in a1:
            driver.find_element(By.ID,"username").clear()
            driver.find_element(By.ID,"username").send_keys(i[0])
            
            #输入邮箱
            driver.find_element(By.ID,"email").clear()
            driver.find_element(By.ID,"email").send_keys(i[1])
            
            #输入密码
            driver.find_element(By.ID,"password").clear()
            driver.find_element(By.ID,"password").send_keys(i[2])
           
            #再次输入密码
            driver.find_element(By.ID,"repassword").clear()
            driver.find_element(By.ID,"repassword").send_keys(i[3])
            
            #点击立即注册
            driver.find_element(By.LINK_TEXT,"立即注册").click()
            
            yq = i[4]
            sj = driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[1]/dd/span/font').text
            if yq == sj:
                print("pass")
            else:
                print("no pass")
                
        driver.quit()
           
#反向注册———>邮箱（不符合邮箱格式要求）
def fxzcyx():
        #创建对象
    driver = webdriver.Chrome()
    #对象打开浏览器网址
    driver.get("http://39.101.167.251/qftest/")
    #点击免费注册
    driver.find_element(By.LINK_TEXT,"免费注册").click()
    #延时1秒
    time.sleep(1)
    with open(r"zidonghua\yxzc.csv","r",encoding="utf-8") as f:
        a1=csv.reader(f)
        for i in a1:
            driver.find_element(By.ID,"username").clear()
            driver.find_element(By.ID,"username").send_keys(i[0])
            
            #输入邮箱
            driver.find_element(By.ID,"email").clear()
            driver.find_element(By.ID,"email").send_keys(i[1])
            
            #输入密码
            driver.find_element(By.ID,"password").clear()
            driver.find_element(By.ID,"password").send_keys(i[2])
            
            #再次输入密码
            driver.find_element(By.ID,"repassword").clear()
            driver.find_element(By.ID,"repassword").send_keys(i[3])
            
            #点击立即注册
            driver.find_element(By.LINK_TEXT,"立即注册").click()
            
            yq = i[4]
            sj = driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[2]/dd/span/font').text
            if yq == sj:
                print("pass")
            else:
                print("no pass")
                
        driver.quit()
        
        
#反向注册———>密码（5位、33位、密码为空）
def fxzcmm():
        #创建对象
    driver = webdriver.Chrome()
    #对象打开浏览器网址
    driver.get("http://39.101.167.251/qftest/")
    #点击免费注册
    driver.find_element(By.LINK_TEXT,"免费注册").click()
    #延时1秒
    time.sleep(1)
    with open(r"zidonghua\mmzc.csv","r",encoding="utf-8") as f:
        a1=csv.reader(f)
        for i in a1:
            driver.find_element(By.ID,"username").clear()
            driver.find_element(By.ID,"username").send_keys(i[0])
            
            #输入邮箱
            driver.find_element(By.ID,"email").clear()
            driver.find_element(By.ID,"email").send_keys(i[1])
            
            #输入密码
            driver.find_element(By.ID,"password").clear()
            driver.find_element(By.ID,"password").send_keys(i[2])
            
            #再次输入密码
            driver.find_element(By.ID,"repassword").clear()
            driver.find_element(By.ID,"repassword").send_keys(i[3])
            
            #点击立即注册
            driver.find_element(By.LINK_TEXT,"立即注册").click()
            
            yq = i[4]
            sj = driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[3]/dd/span/font').text
            if yq == sj:
                print("pass")
            else:
                print("no pass")
                
        driver.quit()
        
#反向注册———>重新输入密码（两次密码不一致）
def fxzcmmcx():
    #创建对象打开浏览器
    driver = webdriver.Chrome()
    #对象打开浏览器网址
    driver.get("http://39.101.167.251/qftest/")
    #点击免费注册
    driver.find_element(By.LINK_TEXT,"免费注册").click()
    #延时1秒
    time.sleep(1)
    with open(r"zidonghua\mmzccx.csv","r",encoding="utf-8") as f:
        a1=csv.reader(f)
        for i in a1:
            driver.find_element(By.ID,"username").clear()
            driver.find_element(By.ID,"username").send_keys(i[0])
            
            #输入邮箱
            driver.find_element(By.ID,"email").clear()
            driver.find_element(By.ID,"email").send_keys(i[1])
            
            #输入密码
            driver.find_element(By.ID,"password").clear()
            driver.find_element(By.ID,"password").send_keys(i[2])
            
            #再次输入密码
            driver.find_element(By.ID,"repassword").clear()
            driver.find_element(By.ID,"repassword").send_keys(i[3])
            
            #点击立即注册
            driver.find_element(By.LINK_TEXT,"立即注册").click()
            
            yq = i[4]
            sj = driver.find_element(By.XPATH,'//*[@id="register-form"]/div/dl[4]/dd/span/font').text
            if yq == sj:
                print("pass")
            else:
                print("no pass")
                
        driver.quit()