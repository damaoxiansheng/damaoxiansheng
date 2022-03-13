#导入时间包
import time
#导入selenium下webdriver模块
from selenium import webdriver

#创建一个浏览器对象，浏览器可根据传入参数改变
#getattr的意思是形式参数txt匹配webdriver下的值，如果txt传过来的值是"Chrome",就是webdriver.Chome
def dakai_driver(txt):
    driver = getattr(webdriver, txt)()
    return driver

#创建一个关键字驱动的类
class guanjianzi_qudong:

    #创建一个构造方法，初始化对象，下面用的是上边的方法
    def __init__(self, txt):
        self.driver = dakai_driver(txt)

    #封装输入网址方法
    def wangzhi(self, txt):
        self.driver.get(txt)

    #封装获取元素方法
    def yuansu(self, name, value):
        return self.driver.find_element(name, value)

    #封装输入值的方法
    def shuru(self, name, value, txt):
        self.yuansu(name, value).send_keys(txt)

    #封装一个点击的方法
    def dianji(self, name, value):
        self.yuansu(name, value).click()

    #封装一个延时方法
    def dengdai(self, txt):
        time.sleep(txt)

    #封装退出浏览器方法，资源释放
    def tuichu(self):
        self.driver.quit()
