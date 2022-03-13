""" 
    元组：
        是一种序列类型：有序、可索引、可切片、可重复、不可改变
    元组的定义：
        使用()定义的。
        元组是不可变的，但是元组的元素可以是可变的类型
"""
tuple0=()
print(tuple0)
print(type(tuple0))

tuple1 = (10,20,10,30)
# <class 'int'>
print(tuple1)
print(type(tuple1))

# 可索引、可切片
print(tuple1[2])
print(tuple1[:])

# 不可改变:'tuple' object does not support item assignment
# tuple1[2] = 50
print(tuple1)


tuple3 = (1,2,['a','c'])
tuple3[2][0]="s"
print(tuple3)