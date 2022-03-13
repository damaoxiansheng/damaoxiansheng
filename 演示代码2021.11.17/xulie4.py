'''
    字符串序列：
        是不是有序的
        可以索引
        可以切片
        可以重复
        可变吗？不可以

    练习：从下文中提取hello world
        <html><body><h1>hello world</h1></body></html>



'''
# 变量：是引用，是指向的一个内存地址
# str1 = "abcd"
# str4 = str1 + "ab"


# print(id(str1))
# str1 = 'dcba'
# str2 = 'abcd'
# # id()
# print(id(str1))
# print(id(str2))


str1 = "<html><body><h1>hello world</h1></body></html>"

# 方法1：切片
# 使用find/index获取开始的索引号
start = str1.find("hello world")
# end = str1.find("</h1>")
# end = str1.find("world")+5
end  =start + 11
print(str1[start:end])

# 方法2：split方法
print(str1.split("<h1>")[1].split("</h1>")[0])