'''
    字典中常用的方法：
        1、获取键的方法:keys
        2、获取值的方法；values
        3、同时获取键和值的方法：items
        4、清空字典：clear
        5、复制
        6、fromkeys
        7、get方法，获取值的
        8、删除：pop()
        9、update方法，将一个字典中的键值对，拼接到另外一个字典中

'''
# dict = {1:2,3:4}
dict2 = {"文章":"姚笛","黄晓明":"杨颖","邓超":"孙俪","文章":"马伊利"}
print(dict2.keys())
print(dict2.values())
# [('文章', '马伊利'), ('黄晓明', '杨颖'), ('邓超', '孙俪')]
print(dict2.items())
# dict2.clear()
# 复制字典
dict3 = dict2.copy()
print(dict3)

dict4 = {}.fromkeys({'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'},{'a','c'})
print(dict4)

# 获取字典中键所对应的值
# KeyError: '文章1'
# print(dict2['文章1'])
# 使用get方法查询字典中的键值更安全，如果指定的键不存在则返回空
print(dict2.get("文章1"))


# 删除键值，pop方法参数是键，返回值是对应的值
print(dict2.pop("文章"))

# 增加一个字典数据到另外一个字典中
dict2.update(dict4)
print(dict2)

list1 = ['a','b','c','d']
list2 = [1,2,3,4]
# dict5 = dict(zip(list1,list2))
# print(zip(list1,list2))
# print(dict5)

