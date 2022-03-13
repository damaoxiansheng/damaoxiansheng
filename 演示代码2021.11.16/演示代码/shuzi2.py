'''
    整数的表示法：
        十进制
        二进制:0和1组成，以0b开头
        八进制：0o开头，0~7组成
        十六进制：0x开头，0~9a~f

    python中的进制转换方法：
        将10进制转化为其他进制，42
        oct()
        hex()
        bin()

    对数字类型的数据处理方法，封装在math模块中
        1、导入
        2、调用方法

'''
# print(10)
# print(0b1001)
# print(0o17)
# print(0x1f)

# 先定义一个十进制数据的变量
# a = 42
# 0b101010=32+8+2=42(8421码)
# 0b11101--29
# 0b11010--26
# # 转为二进制
# print(bin(a))
# # 转为八进制
# print(oct(a))
# # 转为十六进制
# print(hex(a))


# 导入模块
import  math
# math.fabs作用：取绝对值
print(math.fabs(-12.23))

# 取比浮点数大的最近整数
print(math.ceil(12.34))

# math.floor()   取比浮点数小的最近整数
print(math.floor(12.4))

# math模块中还定义了pi，是个常量
print(math.pi)


print(ord("A"))