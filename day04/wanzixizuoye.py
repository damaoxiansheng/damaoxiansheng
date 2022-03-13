# 1. 输入成绩，按90/80/70/60分为ABCDE五个等级
# a=int(input("请输入一个成绩:"))
# if 100>=a>=90:
#     print("成绩等级为-->A")
# if 90>a>=80:
#     print("成绩等级为-->B")
# if 80>a>=70:
#     print("成绩等级为-->C")
# if 70>a>=60:
#     print("成绩等级为-->D")
# if a<60:
#     print("成绩等级为-->E")


# 2.x和y的关系满足如下：
# 	x>=3	y = 2x + 1;
# 	-1<=x<3	y = 2x;
# 	x<=-1	y = 2x – 1;
# 	要求：键盘录入x的值，计算出y的并输出。
# x=int(input("请输入x的值:"))
# if x>=3:
#     y = 2*x + 1
#     print(y)
# elif -1<=x<3:
#     y = 2*x
#     print(y)
# elif x<=-1:
#     y = 2*x - 1
#     print(y)

# 3.键盘录入月份的值，输出对应的季节。
# a=int(input("请输入一个月份:"))
# if 6>=a>=4:
#     print("这是春季呢少年!")
# elif 9>=a>=7:
#     print("这是夏季呢少年!")
# elif 12>=a>=10:
#     print("这是秋季呢少年!")
# elif 3>=a>=1:
#     print("这是冬季呢少年!")

# 4.获取三个数据中的最大值(两种方法)
# a=int(input("请输入第一个数据:"))
# b=int(input("请输入第二个数据:"))
# c=int(input("请输入第三个数据:"))
# if c<a>b:
#     print("最大值为:%s"%(a))
# elif c<b>a:
#     print("最大值为:%s"%(b))
# elif b<c>a:
#     print("最大值为:%s"%(c))