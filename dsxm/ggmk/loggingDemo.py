'''
    日志：
        记录脚本运行过程中的一些数据、状态等。
    logging:
        是一个通用的python中的日志模块。
        按照下面__init__中的配置完成logging的初始化。
        就可以直接使用其中的定义的日志写入方法了。
        info--information：消息等级
        debug---调试等级
        error -- 错误等级日志

'''

import logging
import  time
import os
import sys
# 创建一个logger

class setLog():
    def __init__(self):
        self.logger = logging.getLogger('mylogger')
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler('test.log')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    # 记录一条日志
    def setInfo(self,info):
        self.logger.info(info)

    def setDebug(self,info):
        self.logger.debug(info)


    def setError(self,info):
        self.logger.error(info)


# 自定义的日志方法
# 202112061740，文件名，方法名（用例名），成功/失败，xxx
def  zidingyi(*args):
    # 日志文件的存储目录
    pathLog = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))+r"/rzcf/"
    timeStr = time.strftime("%Y%m%d%H%M%S")
    # 用于作为日志文件的名称
    timeStr1 = time.strftime("%Y%m%d")
    filename = pathLog +timeStr1+r".log"
    with open(filename,"a",encoding="utf-8") as f:
        f.write(timeStr)
        for ar in args:
            f.write(","+ar)
        f.write("\n")


if __name__ == "__main__":
    # log = setLog()
    # log.setInfo("this is info log")
    # log.setDebug("this is debug log")
    # log.setError("this is error log")

    # 验证自定义的日志方法
    zidingyi("测试模块","test01","pass","11111111111111")