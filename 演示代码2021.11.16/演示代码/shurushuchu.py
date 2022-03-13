"""
    输入输出是计算机系统的两个重要的组成部分。
    输入：通过键盘输入数据到程序中（扫码等）
    输出：把数据输出到指定的位置，一般控制台，也可以输出到外部文件中


    输入：input--输入的数据都是字符串格式
        先输出提示信息
        然后监听键盘输入
        输入数据，遇到回车则结束监听
        把输入的数据返回并赋值给变量a

    输出：print--将数据输出到终端
        直接输出：print(age)
        格式化输出：print("我的年龄是:%s"%age)

        print("",end="\n")
        \n : 回车换行
        \t ：4个空格、一个tab键

        %s：字符串的占位符
        %d: 数字的占位符
        %s可以接收字符串和数字类型，但是%d不能接收字符串，只能是数字。

"""
# 等号的右侧：先输出提示信息，然后监听键盘输入
# "23"-->数字类型的字符串
# "ab"-->
# int方法的作用：将数字类型的字符串强转为数字类型
age = int(input("请输入你的年龄:"))
name = input("请输入你的姓名：")
# print(age)
# print("我的年龄是：%s"%age,end="    ")
# %d format: a number is required, not str
print("我的年龄是：%s，我的姓名是：%s"%(age,name),end="\n")