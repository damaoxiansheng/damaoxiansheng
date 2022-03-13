'''
    列表的增删改、逆序方法：
    1、给列表增加元素
        append():直接追加元素到列表的末尾
        insert():插入元素到列表
        extend():把一个列表中元素依次追加到另外一个列表中
    
    2、删除列表的元素
        remove(元素)：删除列表中指定的元素
        pop(): 弹出并返回列表的最后一个元素
        del 列表名[索引号]：删除列表中指定索引号的元素

    3、修改元素
        列表名[索引号]=新值
    
    4、逆序方法
        reverse(): 逆序方法

'''
list1 = ["a","b","c","d"]
# list1.append("d")
# list1.insert(1,"f")
# list1.insert(1,[1,2,3])
# list2 = [1,2,3]
# list1.extend(list2)
# print(list1)
# 
# list1.remove("a")
# a = list1.pop()
# print(a)
# a = list1.pop()
# print(a)
# a = list1.pop()
# print(a)

# del list1[2]
# list1[2] = "c"
# print(list1)

# list1.reverse()
# print(list1)
print(list1[::-1])
print(list1)