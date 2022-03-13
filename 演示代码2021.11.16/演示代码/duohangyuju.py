'''

    多行语句：
        解决的是在一行中显示不开太长的符号。
        使用\来实现换行的作用
    空行：
        在方法和方法之间空一行，以增强阅读性
    
    空语句、占位语句：pass
    
'''

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa=12
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb=23
ccccccccccccccccccccccccccccccc=34
d=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa+\
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb+\
    ccccccccccccccccccccccccccccccc
print(d)
# python中使用{}、[]、()来定义的数据，不用\可以直接换行
a = [1,2,3,4,55555555,
67777777777777,88888888,9999999,
333333333333,2222222222,3333333334,
7777777777777777]
print(a)

def aa():
    pass

def bb():
    return 0
    