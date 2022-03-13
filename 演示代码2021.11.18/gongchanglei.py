# int的参数一定要是数字类型的字符串
str1 = "12"
# list1 = [1,2]
# str2 = "ab"
print(int(str1))
# print(int(str2))
# print(int(list1))

# str方法：将其他数据类型转为字符串
int1 = 12
float1 =12.2
list1 = [1,2]
print(str(int1))
print(str(float1))
print(str(list1))

# list方法：将序列转为列表的方法
str2 = "abcdef"
print(list(str2))

tuple1=(1,2,3,4,5)
print(list(tuple1))

# set():不能重复
str3 = "abcabcabc"
list22 = list(str3)

import  random
random.shuffle(list22)
print(list22)