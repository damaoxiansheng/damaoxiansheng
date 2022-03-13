def dl(driver,yhm,yx,mm,qrmm):
    #导包
    from selenium.webdriver.common.by import By
    import time
    #对象打开浏览器网址
    driver.get("http://39.101.167.251/qftest/")
    #点击免费注册
    driver.find_element(By.LINK_TEXT,"免费注册").click()
    #延时1秒
    time.sleep(1)
    #输入用户名
    driver.find_element(By.ID,"username").send_keys(yhm)
    time.sleep(1)
    #输入邮箱
    driver.find_element(By.ID,"email").send_keys(yx)
    time.sleep(1)
    #输入密码
    driver.find_element(By.ID,"password").send_keys(mm)
    time.sleep(1)
    #再次输入密码
    driver.find_element(By.ID,"repassword").send_keys(qrmm)
    time.sleep(1)
    #点击立即注册
    driver.find_element(By.XPATH,"立即注册").click()
    time.sleep(1)

        
        