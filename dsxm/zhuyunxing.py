# 导包
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from ggmk import mailsend

# 报告保存路径
shijian = time.strftime("%Y-%m-%d-%H-%M")
a = os.path.dirname(__file__)
lianjie = a + r"/bgxf/" + shijian + ".html "

# 获取用例的路径
yxlj = os.path.dirname(__file__) + r"/ffcf"

discover = unittest.defaultTestLoader.discover(yxlj, pattern="ds*.py")

with open(lianjie, "wb") as f:
    yx = HTMLTestRunner(f, title="刘有韦自动化运行报告运行报告", description="第nnn次运行的结果")
    yx.run(discover)
    # 设置邮件发送
    yxfs = mailsend.mailsend()
    yxfs.sendFujian(shijian)
