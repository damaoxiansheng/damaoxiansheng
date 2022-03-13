# 1、1~100奇数求和。
# a=0
# for i in range(1,101):
#     if i%2!=0:
#         a+=i
# print(a)

# 2、1~100偶数求和。
a = 0
for i in range(1, 101):
    if i % 2 == 0:
        a += i
print(a)

# 3、对于一个四位的整数，倒序输出其每一位上的数字。例如，一个整数3421，分别显示和输出：1,2,4,3。
# a=list(input("请输入一个四位数整数:"))
# print("%s,%s,%s,%s"%(a[3],a[2],a[1],a[0]))

# 4、将一个十进制的整数，转化为二进制，倒序输出该二进制的每一位数字。例如，十进制的10，转化为二进制是1010，倒序输出：0,1,0,1.

# a=int(input("请输入一个二进制整数"))
# b=bin(a)
# c=list(b[2:])
# print(','.join(c[::-1]))

# 5、百钱白鸡。公鸡5钱一只，母鸡3钱一只，小鸡1钱3只。问100钱买100只鸡。分别怎么购买。

# for gj in range(1,21):
#     for mj in range(1,34):
#         for xj in range(3,100,3):
#             if gj+mj+xj==100 and gj*5+mj*3+xj/3==100:
#                 print("公鸡%s只,母鸡%s只,小鸡%s只"%(gj,mj,xj))


""" 6、求解10000以内的四叶玫瑰数。四叶玫瑰数指的是一个四位数，每一位上的数字的4次方的求和等于这个四位数。
        例如，1634=1*1*1*1+6*6*6*6+3*3*3*3+4*4*4*4。那么1634就是一个四叶玫瑰数。
"""
# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             for d in range(0,10):
#                 f=int("%s%s%s%s"%(a,b,c,d))
#                 if f==a**4+b**4+c**4+d**4:
#                     print("四叶玫瑰数是%s"%(f))
# 7、假设纸的厚度是1/1000厘米，折叠多少次能够超过到达月球。地月距离是38万公里。
# dyjl=float(38000000000)
# houdu=1/1000
# a=0
# while True:
#     cj=houdu**a*2
#     if cj==dyjl:
#         break
#     a=a+1
# print(cj)

# n = 0
# while True:
#     thk = 1/1000 * 2 ** n
#     if thk >= 38000000000:
#         break
#     n += 1
# print(n)


# 1. 设计一个重量转换器，输入以'g'为单位的数字后返回换算成'kg'的结果

# def zlzh(g):
#     kg=g/1000
#     print("%s千克"%(kg))
# zlzh(50000)


# 2. 设计一个求直角三角形斜边长（hypotenuse）的函数
# def xbc(a,b):
#     c=a^2+b^2
#     return c^2

# print("斜边长是:%s"%(xbc(7,9)))

# 3. 定义一个学生注册函数enroll()，打印学生姓名，性别，年龄，城市， 使用默认参数降低调用函数的复杂度

# def enroll(name,sex,age,cs="北京"):
#     print(name,sex,age,cs)

# enroll("张三","男",18)

"""
 4. 设计一个复利的计算函数 invest(), 它包含三个参数：amount(资金) rate（利率），time（投资时间 年单位）,
       输入每个参数后调用函数，应该返回每一年的资金总额，假设利率为5%
       """


def invest(amount, rate, time):
    ze = amount*rate*time+amount
    return ze


print(invest(10000, 0.05, 1))


# 5.定义一个函数，计算给定一组数字a，b，c...，请计算a^2 + b^2 + c^2 +...

# def js(*a):
#     b=0
#     for i in a:
#         b+=i
#     return b

# print(js(2,4,3))


"""
6.完成一个方法：游戏中经常会从一个点（x,y）移动到另外一个点(nx,ny)，给出坐标、位移和角度，
就可以计算出新的坐标位置（nx,ny），根据上面需求，设计一个move方法，实现返回新坐标的功能
"""
