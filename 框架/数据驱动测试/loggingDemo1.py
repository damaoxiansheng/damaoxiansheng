"""
    日志：
        记录脚本运行过程中的一些数据、状态等。
    logging:
        是一个通用的python中的日志模块
        按照下面__init__中的配置完成logging的初始化
        就可以直接使用其中的定义的日志写入方法了
        
"""


import logging
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