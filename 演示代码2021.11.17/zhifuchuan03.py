"""
    字符串的常见处理方法：
        获取索引位置： str.index()
            获取字符串中指定字符的下标或者索引号
            字符串的索引号是从0开始的，总长度-1是最大编号
        去除结尾空格： str.rstrip()
        去除开头空格： str.lstrip()
        去除两端空格： str.strip()
        将首字母大写： str.title()
        分隔返回列表： lst = str.split("-")
        将字符串转为小写：str.lower()
        将字符串转为大写：str.upper()


"""
str1 = "  ABCDEF  TGMMDA   "
print(str1.index("DE"))
# 去除结尾空格
# print(str1.rstrip())
# # print(str1)
# # 去除开头空格： str.lstrip()
# print(str1.lstrip())

print(str1.strip())
print(str1.lower())
str2 = "abcdefg"
print(str2.title())
print(str2.upper())



# 分隔字符串
str3 = "186-2198-4010"
print(str3.split("-"))
