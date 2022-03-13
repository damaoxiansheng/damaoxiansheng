from selenium import webdriver
import time

# #不调用浏览器无头运行
# from selenium.webdriver.chrome.options import Options
# opts = Options()
# opts.headless= True
# a = webdriver.Chrome(options=opts)
a = webdriver.Chrome()
time.sleep(1)
a.get("https://tieba.baidu.com/index.html")
time.sleep(1)
# a.find_element_by_id("kw").send_keys("刘有韦")
#第二种写法（只支持selenium4.0以上）
# a.find_element(by="id",value="kw").send_keys("刘有韦")
#第三种写法，需要导入包
from selenium.webdriver.common.by import By
# a.find_element(By.ID,"kw").send_keys("刘有韦")
# a.find_element(By.XPATH,"/html/body/div/div/div[5]/div/div/form/span[2]/input").click()
a.find_element(By.XPATH,"//*[@id='day_rcmd']/div[1]/div/div/p[1]/a").click()
# a.find_element(By.LINK_TEXT,"赛博朋克2077吧").click()



# a.find_element(By.PARTIAL_LINK_TEXT,"女人").click()
# time.sleep(5)
a.quit()


