'''
    登录后，更新个人中心资料。
        登录账号（模块）
        切换到个人资料
        修改个人资料
        更新资料
        退回用户中心
        点击退出登录（模块）

'''
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import  time
import unittest
# 还希望日志功能（在public下）
import  os
import sys
# 先把public做成包，只需要把当前文件的上级目录（verydows电商）加到python导包检索目录中
# 如何获取verydows电商目录
pathCurrent = os.path.abspath(os.path.dirname(__file__))
pathUp = os.path.abspath(os.path.dirname(pathCurrent))
sys.path.append(pathUp)
from public.loggingDemo import setLog,zidingyi
from public.loginlogout import login,logout

class verydows_info_update(unittest.TestCase):
    def setUp(self):
        self.driver =  webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # 登录
        login(self.driver)

    def avtest_update_01(self):
        # 点击个人资料
        self.driver.find_element(By.LINK_TEXT,"个人资料").click()
        # 设置昵称
        self.driver.find_element(By.ID,"nickname").clear()
        self.driver.find_element(By.ID,"nickname").send_keys("allen")
        # 设置qq
        self.driver.find_element(By.ID,"qq").clear()
        self.driver.find_element(By.ID,"qq").send_keys("287939828")       
        # 设置线性别
        # //*[@id="profile-form"]/dl[3]/dd/label[1]/input  
        self.driver.find_element(By.XPATH,'//*[@id="profile-form"]/dl[3]/dd/label[1]/input').click()
        # 设置
        self.driver.find_element(By.XPATH,'//*[@id="birth_year"]/option[80]').click()
        self.driver.find_element(By.XPATH,'//*[@id="birth_month"]/option[8]').click()
        self.driver.find_element(By.XPATH,'//*[@id="birth_day"]/option[8]').click()
        # 点击更新资料
        self.driver.find_element(By.XPATH,'//*[@id="profile-form"]/div/button').click()
        # /html/body/div/div[2]/h3
        # 断言
        try:
            expectValue = "更新资料成功"
            actualValue = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/h3').text
            self.assertEqual(expectValue,actualValue)
        except:
            filename = __file__.split("/")[-1]
            zidingyi(filename,self._testMethodName,expectValue,actualValue,"测试执行失败")
        finally:
            logout(self.driver)

    # 更新头像
    def test_update_img(self):
        # 点击个人资料
        self.driver.find_element(By.LINK_TEXT,"个人资料").click()
        # input标签的上传功能，可以使用send_keys()直接上传即可
        # //*[@id="avatar-form"]/input[1]
        self.driver.find_element(By.XPATH,'//*[@id="avatar-form"]/input[1]').send_keys(r"e:/data/downloadImage.jpg")
        time.sleep(2)
        # 图片剪切
        self.driver.find_element(By.XPATH,'//*[@id="save-avatar-btn"]').click()
        time.sleep(5)
        # 更细资料
        self.driver.find_element(By.XPATH,'//*[@id="profile-form"]/div/button').click()
        try:
            expectValue = "更新资料成功"
            actualValue = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/h3').text
            self.assertEqual(expectValue,actualValue)
        except:
            filename = __file__.split("/")[-1]
            zidingyi(filename,self._testMethodName,expectValue,actualValue,"测试执行失败")
        finally:
            logout(self.driver)


        def tearDown(self):
            self.driver.quit()   

if __name__=="__main__":
    unittest.main()