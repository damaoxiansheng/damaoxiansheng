import unittest
from HTMLTestRunner import HTMLTestRunner
import time

sfm = time.strftime("%Y-%m-%d-%H-%M")
discover = unittest.defaultTestLoader.discover("D:/pythonzuoye/jiekoukuangjia/", pattern="ceshi.py")

with open("D:/pythonzuoye/jiekoukuangjia/"+sfm+".html", "wb") as f:
    yx = HTMLTestRunner(f, title="刘有韦接口自动化运行报告运行报告", description="第1次运行的结果")
    yx.run(discover)