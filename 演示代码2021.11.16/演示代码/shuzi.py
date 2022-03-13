'''
    数字类型（Number）：
        整数类型：
            python中的整数没有长度限制，只要内存能放的下即可。
        浮点数类型:
            1.234、1.23456888888888888888888888889234235
            python中的浮点型数据只保留其17位有效数字
        布尔类型:
            只有两个值，True、False，是两个关键字
        复数:
            1+2j

'''
# a=12
# b=2222222222222222222222222222222222222222222222222222222222222222
# age = 40
# # 支持科学记忆法
# c = 3e+10
# d = 2E-3
# float1 = 12.234
# # 1.2345688888888888
float2 = 1.234567891234567123
print(float2)

b = 10/3
print(b)

# 要保留到30位
from  decimal import Decimal,getcontext
getcontext().prec = 30
a = Decimal(10)/Decimal(3)
print(a)

flag1 = True
flag2 = False
print(flag2)

c = 1+2j
print(c)