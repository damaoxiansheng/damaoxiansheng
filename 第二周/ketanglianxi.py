# 公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱
for gj in range(1, 20):
    for mj in range(1, 33):
        for xj in range(1, 100):
            if gj + mj + xj == 100 and gj * 5 + mj * 3 + xj / 3 == 100:
                print("公鸡有%s只,母鸡有%s只,小鸡有%s只" % (gj, mj, xj))


def fanzhuan(a, b):
    c = a
    a = b
    b = c
    return a, b


a = 28
b = 42
a, b = fanzhuan(a, b)

print(a, b)


def sx(a, b):
    c = {"a": "公牛", "b": "母牛"}
    print("hello,%s同志,你是一头%s" % (a, c.get(b)))


sx("杨中申", "b")


# def yahou (a, b, c, d="撸管子"): (a, b, c, d)

# print("学生姓名是:%s,年纪:%s,性别:%s,爱好:%s" %

# yahou("张云辉", 18, "男", d ="放屁" )


def bdc(*a):
    b = 0
    for i in a:
        b = b + i
    return b


print(bdc(1, 5, 3, 2, 6, 3))

a = {1: 5, 3: 2, 6: 3}
for i in a.values():
    print(i)

a = 1

