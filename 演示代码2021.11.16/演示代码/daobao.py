'''
    导包（模块）：
        希望要用别人已经写好的py文件中代码。
        from
        import
        as
    需求：想用time模块中的sleep方法。
          time模块中还有一个方方法：strftime
        import time
        from time import sleep
        from time import sleep,strftime
        from time import sleep as xm

'''
# import time
# time.sleep(5)
# atime = time.strftime("%Y-%m-%d")
# print(atime)

# from time import sleep,strftime
# sleep(5)
# atime = strftime("%Y-%m-%d")
# print(atime)

# from time import sleep as xm
# xm(3)

# 当前目录中的模块是可以直接导入的
# 还可以导入python安装目录下的自带或者第三方的py文件
# 包：就是一个文件夹，里面要有一个__init__.py的文件
# import test01
# test01.aaa()

from test01 import aaa
aaa()