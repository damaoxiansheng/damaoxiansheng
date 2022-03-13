# 1.将"hello world"转换为首字母大写"Hello World"。
# a="hello world"
# print(a.replace("h", "H"))
# 2.如何检测字符串中只含有数字,True代表都是数字？
# a="1"
# b=a.isdigit()
# print(b)
# print(int(b))
# 3.如何将一串字符串进行反转
# a="hello world"
# print(a[::-1])
# 4.如何去掉字符串的前后空格？
# a="   hello world  "
# print(a.strip())
# 5.获取字符串的最后两个字符。
# a="hello world"
# print(a[-2:])
# 6.将字符串转换为小写。
# a = "HELLO WORLD"
# print(a.lower())
# 7、List = [1,2,2,1,3,4,5,4]，对 List 列表元素去重
List1 = [1, 2, 2, 1, 3, 4, 5, 4]
list2 = set(List1)
list3 = list(list2)
print(list3)
# 8.实现 "1,2,3" 变成 ["1","2","3"]
# a="1,2,3"
# b=a.split(",")
# print(b)
# 9.随机打乱一个列表A=[1,2,3,4,5]的元素。
# import random
# A=[1,2,3,4,5]
# random.shuffle(A)
# print(A)
# 10.如何交换字典的键和值
# a={"a":1,"b":2,"c":3}
# print(dict(zip(a.values(),a.keys())))



# 已知字典dt = {"name":"zhangsan","password":"123456"}
# dt = {"name":"zhangsan","password":"123456"}
# (1)增加key值"iphone",并赋值"13109877890"
# dt.update({"iphone":"13109877890"})
# print(dt)
# (2)获取字典中所有的key值
# print(dt.keys())
# (3)获取字典中所有的value值
# print(dt.values())
# (4)获取字典中所有的键值对
# print(dt.items())
# (5)删除key为"iphone"的值
# dt.pop("iphone")
# print(dt)
