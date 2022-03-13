'''
    项目目录分层机制：
        public：公共的模块，比如登录、退出、邮件、日志、数据库处理等
        test_cases: 分模块管理测试用例
            verydows_reg_username.py
            verydows_reg_email.py
            verydows_login_true.py
            verydows_login_fan.py
            verydows_info_touxiang.py
            verydowsBack_login.py

        test_datas:放参数化数据的（读操作）
            csv、json、excel
        
        test_reports: 存放测试执行报告
            html格式可视化报告
        
        test_logs:存放日志的（写操作）
            文本文件的写入，追加写入
        
        maintest.py: 主运行文件
            测试用例管理
            测试用例执行
            发送测试结果

'''
import unittest
import os
import sys
from HTMLTestRunner import HTMLTestRunner
import time
from public.mailsend import mailsend
# 加载一个测试集合
pathCase = os.path.abspath(os.path.dirname(__file__))+r"/test_cases/"
# 加载verydows开头，py结尾的所有模块中自动化测试用例
discover = unittest.defaultTestLoader.discover(pathCase,pattern="verydows*.py")

# 输出报告，报告放在哪，叫什么名字
pathReport = os.path.abspath(os.path.dirname(__file__))+r"/test_reports/"
timeStr = time.strftime("%Y-%m-%d-%H-%M-%S")
filename = pathReport+timeStr+r".html"

# HTMLTextRunner运行
with open(filename,"wb") as f:
    runner = HTMLTestRunner(f,title="测试执行报告",description="第一次执行结果")
    runner.run(discover)

# 创建以邮件发送的对象
ms = mailsend()
# 将生成的报告文件发送到指定的邮箱
ms.sendFujian(timeStr)