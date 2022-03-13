'''
    序列通用的运算符：
        +：连接运算，可以把两个序列拼接在一起
            str1 = "abc"
            str2 = "efg"
            str3 = str1 + str2
        
        *: 复制运算，就是把序列复制几份
            str1 * 2
        
        in ：成员运算符，就是判断某个元素（成员）是不是序列的成员。
            "a" 是 "abc" 的成员吗？
            "ab"是 "abc" 的成员吗？
            "ac"是 "abc" 的成员吗？
        not in：成员运算符，就是判断某个元素（成员）是不是 不是序列的成员。

        str[索引号]：
            正向和反向索引 
                 
        str[start:end:step]:
            正向和反向索引
'''
str1 = "abc"
str2 = "efg"
str3 = str1 + str2
print(str3)
str4 = str1 * 10
print(str1)
print(str4)

print('a' in str1)
print('ab' in str1)
print('ac' in str1)

print('a' not in str1)
print('ab' not in str1)
print('ac' not in str1)


# string index out of range
# print(str3[8])
# 取全部
print(str3[:])
print(str3[::])
# 从第三个元素切片到结尾
print(str3[2:])
print(str3[2:8])

# 逆序
print(str3[::-1])