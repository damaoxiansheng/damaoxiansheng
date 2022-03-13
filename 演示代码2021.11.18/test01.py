'''
已知字符串s = "I’m learning Python,my name is xiaobai!"
    (1)截取字符串(切片)
        截取第一位到第三位的字符；
        截取字符串的全部字符；
        截取第七个字符到结尾；
        截取从头开始到倒数第三个字符之前；
        截取第三个字符；
        截取倒数第一个字符；
        创造一个与原字符串顺序相反的字符串；
        截取倒数第三位到结尾；
    (2)字符串函数
        获取“l”的索引；
        查找“Python”在字符串中的位置；
        获取“n”出现的次数；
        获取字符串“xiaobai”；
        把“xiaobai”替换成自己的名字；
        把字母转换成大写；
'''
s = "I’m learning Python,my name is xiaobai!"
# 截取第一位到第三位的字符
print(s[0:3])
# 截取字符串的全部字符
print(s[:])
print(s[0:])
print(s[0:50:])

# 截取第七个字符到结尾
print(s[6:])

# 截取从头开始到倒数第三个字符之前
print(s[-len(s):-3])
print(s[0:len(s)-3])

# 截取第三个字符；
print(s[2])
print(s[2:3])

# 截取倒数第一个字符；
print(s[len(s)-1])
print(s[-1])

# 创造一个与原字符串顺序相反的字符串(反转字符串)
# print(s[::-1])
print("".join(reversed(s)))

# print(''.join(reversed(s)))


# 截取倒数第三位到结尾；
# print(s[-3:])

# 获取l的索引
# print(s.index("l"))
# print(s.find("l"))

# print(s.index("Python"))
# print(s.find("Python"))

# 获取“n”出现的次数；
# print(s.count("n"))
# 获取字符串“xiaobai”；
# print(s[s.find("xiaobai"):s.find("xiaobai")+7])
# print(s.split(" ")[-1].split("!")[0])
# print(s.split(" ")[-1][0:len("xiaobai")])

# 把“xiaobai”替换成自己的名字；
# print(s.replace("xiaobai","allen"))
# 把字母转换成大写；
# print(s.upper())