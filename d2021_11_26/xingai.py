import csv

#创建一个读取的方法
def dq_csv():
    list2 = []
    with open(r"D:\pythonzuoye\ygxx.csv","r",encoding="utf-8") as f:
            a1=csv.reader(f)
            for i in a1:
                list2.append(i)
    return list2

#创建一个写入的方法
def xr_csv(list1):
    with open(r"D:\pythonzuoye\ygxx.csv","a",encoding="utf-8",newline="\n") as f:
            a1=csv.writer(f)
            a1.writerow(list1)


#创建一个写入的方法
def xr_csv2(list3):
    with open(r"D:\pythonzuoye\ygxx.csv","w",encoding="utf-8",newline="\n") as f:
            a1=csv.writer(f)
            a1.writerows(list3)
#把读取功能赋值给一个变量
a3=dq_csv()
#死循环

while True:
    list1 = []
    del list1[::]
    #主界面显示菜单
    print("=========================学员管理菜单==========================\n1-增加       2-更新      3-删除学员      4-查询        5-退出\n===============================================================")
    #设置一个变量，接受输入数据
    a=int(input("====================请输入您要执行的功能：=====================\n"))
    #如果等于菜单1：增加功能则列表list1接受的值
    if a == 1:
        #输入值
        list1.append(input("请输入姓名："))
        list1.append(input("请输入性别："))
        list1.append(input("请输入出生日期："))
        list1.append(input("请输入班级："))
        list1.append(input("请输入学号："))
        #赋值一个变量，为了下一步不重复执行
        static = 1
        #遍历csv文件
        for i in a3:
            print(i)
            #如果文件学号等于我输入的值，则报学号重复！
            if list1[4] in i:
                static = 0
                print("学号重复！")
        #如果不等于csv文件学号，则插入此条数据
        if static:
            xr_csv(list1)
            
    elif a == 2:
        gxxm=input("请输入要删除学员姓名：")
        for k,i in enumerate(a3):
            # print(k,i,gxxm)
            if i[0] == gxxm:   
                a3.pop(k)
        list1.append(input("请输入姓名："))
        list1.append(input("请输入性别："))
        list1.append(input("请输入出生日期："))
        list1.append(input("请输入班级："))
        list1.append(input("请输入学号："))
        #赋值一个变量，为了下一步不重复执行
        static = 1
    
        #遍历csv文件
        for i in a3:
            #如果文件学号等于我输入的值，则报学号重复！
            if list1[4] == i[4]:
                static = 0
                print("学号重复！")
        #如果不等于csv文件学号，则插入此条数据
        if static:
            xr_csv(list1)
           
    elif a == 3:
        list3=[]
        with open(r"D:\pythonzuoye\ygxx.csv","r",encoding="utf-8") as f:
            a5=csv.reader(f)
            gxxm=input("请输入要删除学员姓名：")
            for ddd in a5:
                list3.append(ddd)
                for i in list3:
                    if gxxm in i:
                        print(i)
                        list3.remove(i)
                    xr_csv2(list3)
            
    elif a == 4:
        with open(r"D:\pythonzuoye\ygxx.csv","r",encoding="utf-8") as f:
            a6=csv.reader(f)
            for i in a6:
                print(i)
    
    elif a == 5:
        break