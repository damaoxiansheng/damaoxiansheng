'''
    列表：
        是一种序列类型，可以存放各种数据类型的（容器类型）
        列表中可以放数字、字符串、列表、元组、字典等

        有序、可重复、可切片、可索引、可变

    列表的定义：列表名 = [元素1,元素2,元素n...]

'''
list1 = [1,2,3,4,5,6]
list2 = ["a","b","b","d","a","b","b","d","a","b","b","d","a","b","b","d"]
print(list2[0])
print(list2[-1])
# list index out of range
# len(list2): 长度，也表示列表元素的个数
print(list2[len(list2)-1])
# 切片的结果是一个列表
print(list2[0:3])
# 给列表更新数据
list2[0] = "f"
print(list2)

# 列表运算符
list3 = ["a","b","b","d",1,2,3,[1,3,4]]
print(1 in list3)
print(1 not in list3)
print("a" in list3)
print([1,3,4] in list3)

list4 =list1 + list2
print(list4)

list5 =list1 * 3
print(list5)

