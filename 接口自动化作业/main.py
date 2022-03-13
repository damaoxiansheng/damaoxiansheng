# 导包
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from gonggong import mailsend

# 报告保存路径
shijian = time.strftime("%Y-%m-%d-%H-%M")
a = os.path.abspath(os.path.dirname(__file__))
lianjie = a + r"/baogao/" + shijian + ".html "

# 获取用例的路径
yxlj = os.path.abspath(os.path.dirname(__file__)) + r"/yonglicunfang"

discover = unittest.defaultTestLoader.discover(yxlj, pattern="ceshi_qiantai*.py")

with open(lianjie, "wb") as f:
    yx = HTMLTestRunner(f, title="刘有韦接口自动化运行报告", description="第nnn次运行的结果")
    yx.run(discover)
    # 设置邮件发送
    yxfs = mailsend.mailsend()
    yxfs.sendFujian(shijian)
