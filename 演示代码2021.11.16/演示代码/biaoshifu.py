'''
    标识符：
        python语言中给变量、常量、方法、类、文件名等起的名字。
        a = 1
    标识符的组成：
        是由数字、字母、下划线组成的
        数字不能开头
        大小写敏感

        123 = 12
        A12——23 =23
        a_123=123
        A = 12
        a = 12
    文件名的命名要求：
        不允许是数字开头
        不允许出现汉字
        不允许使用python自带的模块的名字(time.py屏蔽python安装目录下的的time模块)
    
    标识符的命名规范：
        见名知义：name、age、xingming、nianling
        驼峰式的命名规范：name、studentName、teacherId、student_name、teacher_id
        python中推荐使用：name、student_name、teacher_id
        不能是关键字：if、for等不能作为标识符

    
'''
# a = 12
# A = 23
# # A12——23 =23
# import time
# import pymysql
# import  sys

# print(sys.path)
# # time.sleep(5)

import  pymysql