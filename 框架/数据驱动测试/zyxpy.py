import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import mailsend

shijian = time.strftime("%Y-%m-%d-%H-%M")
lj = "D:/pythonzuoye/框架/数据驱动测试/" + shijian + ".html"

a=unittest.defaultTestLoader.discover(r"D:\pythonzuoye\框架\数据驱动测试",pattern="d20211206*.py")

with open(lj,"wb") as f:
    b = HTMLTestRunner(f,title="测试报告")
    b.run(a)
aa = mailsend.mailsend()
aa.sendFujian(shijian)