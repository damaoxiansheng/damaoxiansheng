from selenium import webdriver
class fangfa:

    def __init__(self, driver):
        self.driver = driver

    def dingwei(self, dingwei, yuansu):
        return self.driver.find_element(dingwei, yuansu)

    def dianji(self, dingwei, yuansu):
        return self.dingwei(dingwei, yuansu).click()

    def shuru(self, dingwei, yuansu, txt):
        return self.dingwei(dingwei, yuansu).send_keys(txt)