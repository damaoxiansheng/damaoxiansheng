import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

path = os.path.dirname(__file__)
time1 = time.strftime("/%Y-%m-%d-%H-%M") + ".html"
lianjie = path + time1

discover = unittest.defaultTestLoader.discover(path, "test*.py")

with open(lianjie, "ab") as f:
    yx = HTMLTestRunner(f, title="运行报告")
    yx.run(discover)
