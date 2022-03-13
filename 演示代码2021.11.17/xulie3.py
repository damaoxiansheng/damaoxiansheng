'''
    序列通用方法：
        index() : 获取序列的元素的索引号
            序列名称.index(元素)
            序列名称.index(元素,start,end)
        min()/max(): 获取序列中最小元素，比较的是ascii码的大小
            A：65
            B：66
            a：97
            b：98
        len() : 是获取序列长度的方法
            len(str1)
        count(): 计算并返回指定的元素的个数的
            str1 = "ABCDDDEFDD"
            序列名.count(元素)
'''
str1 = "ABCDDCEFC"
print(str1.index("C"))
print(str1.index("CD"))
# substring not found
# print(str1.index("CF"))
# print(str1.index("C",4,6))
# find不是通用方法，是字符串特有的。
# 找不倒子串返回-1；如果找到了呢返回索引
print(str1.find("CD"))
print(str1.find("CF"))


str2 = "123456"
# min()的用法
print(min(str2))
print(max(str2))

print(len(str1))
print(str1.count("C"))