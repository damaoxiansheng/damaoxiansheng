'''
    集合类型：
        不是序列类型，是无序、不可重复的数据结构

    集合定义：
        使用{}
'''
set1 = {10,20,30,10}
# <class 'dict'>
# print(type(set1))
print(set1)


set2 = {"a","b","c","d"}
set3 = {"f","b","c","d",'e'}
# 差集运算
print(set3-set2)
# 并集运算
print(set3 | set2)

# 交集运算
print(set3 & set2)

list1=[1,2,3,1,2,3]
set4 = set(list1)
print(set4)


studentSex = {"男","女"}
print(studentSex.update("好"))
#{'好', '男', '女'}
print(studentSex)