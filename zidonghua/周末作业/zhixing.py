"""
    执行文件
"""
#导入unittest框架
import unittest
from HTMLTestRunner import HTMLTestRunner
import time


shijian = time.strftime("%Y-%m-%d-%H")+".html"
lj = r"zidonghua/周末作业/" + shijian


#匹配文件下所有jsq的py文件
discover = unittest.defaultTestLoader.discover(r"zidonghua\周末作业",pattern="jsq*.py")

# # #执行文件，且信息保存在指定文件
# # with open(r"D:\pythonzuoye\zidonghua\周末作业\jieguo.txt","w",encoding="utf-8") as f:
# #     a = unittest.TextTestRunner(f,descriptions=True,verbosity=3)
# #     a.run(discover)

#执行文件结果生成HTML文件
with open(lj,"ab") as f:
    a = HTMLTestRunner(f,title="测试报告",description="第一次运行的结果")
    a.run(discover)