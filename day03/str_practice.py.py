"""
# 已知字符串s = "I’m learning Python,my name is xiaobai!"
# (1)截取字符串
s = "I’m learning Python,my name is xiaobai!"
# 	截取第一位到第三位的字符；
print(s[1:3])
# 	截取字符串的全部字符；
print(s[::])
# 	截取第七个字符到结尾；
print(s[7:])
# 	截取从头开始到倒数第三个字符之前；
print(s[7:-3])
# 	截取第三个字符；
print(s[3])
# 	截取倒数第一个字符；
print(s[-1::])
# 	创造一个与原字符串顺序相反的字符串；
print(s[::-1])
# 	截取倒数第三位到结尾；
print(s[-3:])
# (2)字符串函数
# 	获取“l”的索引；
print(s.index("l"))
# 	查找“Python”在字符串中的位置；
print(s.index("Python"))
# 	获取“n”出现的次数；
print(s.count("n"))
# 	获取字符串“xiaobai”；
hei=(s.split("is")[1].split("!")[0])
print(hei.lstrip())
# 	把“xiaobai”替换成自己的名字；
#第一种
b=s.split(" ")[1].split("!")[0]
c="liuyouwei"
print(c)
# 	把字母转换成大写；
print(s.upper())
# 一个网页的HTML源码。其中有一段：
# 	<html><body><h1>hello world</h1></body></html>
# 	想要把这个hello world提取出来，用python的字符串处理，如何处理？
bibi="<html><body><h1>hello world</h1></body></html>"
print(bibi.split("<h1>")[1].split("</h1>")[0])


# 要求：完成以上任务，保存文件名为str_practice.py
"""


# 已知列表 L = ['apple','pear','banana','oranger','grape']
# (1) 往列表L中追加“peach”
# L = ['apple','pear','banana','oranger','grape']
# L.append("peach")
# print(L)
# (2) 定义另外一个列表L1 = [1,2,"A","B"],将该列表追加至L中
# L1 = [1,2,"A","B"]
# L.insert(0, L1)
# print(L)
# (3) 向列表L开头添加“fruit:”
# L.insert(0, "fruit:")
# print(L)
# (4) 获取列表L的总长度
# print(len(L))
# (5) 删除列表L的最后一个元素（使用两种方法）
#方法一：
# del(L[4])
# print(L)
#方法二：
# L.pop()
# print(L)
# (6) 删除列表的第5个元素
# del(L[4])
# print(L)
# (7) 删除元素“A”
# L[0].remove('A')
# print(L)

# 已知列表 L2 = [2,1,4,5,4]
# (1)对列表L2进行排序--sort()
L2 = [2,1,4,5,4]
L2.sort(reverse=True)
# print(L2)
# print(L2.sort())
# (2)获取列表中的最大值和最小值
# print(min(L2))
# print(max(L2))
# (3)对排序好的列表进行逆序排列（使用两种方法）
# print(L2[::-1])
L2.sort()
print(L2[::-1])
print(L2)

