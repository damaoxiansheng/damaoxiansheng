'''
    在控制台输入一个老师的姓名、职位和家庭住址信息（input）
    使用一个print方法输出如下信息：（多行显示）
    ==============================================
    姓名：xx
    职位：xx
    家庭住址：xx
    ==============================================

'''
a=input("姓名：" )
b=input("职位： ")
c=input("住址:  ")
print("==============================================\n\
姓名：%s\n\
职位：%s\n\
住址：%s\n\
=============================================="%(a,b,c))

# 定义了一个方法
def aaa():
    print("hello world")
