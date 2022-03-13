#导入csv
import csv
#创建一个列表，作为后续插入csv文件列表
list1=[{"姓名":"张云辉"},{"性别":"男"},{"出生日期":"2020.11.12"},{"班级":"2104"},{"学号":"0001"}]
#死循环
while True:
    #主界面显示菜单
    print("=========================学员管理菜单==========================\n1-增加       2-更新      3-删除学员      4-查询        5-退出\n===============================================================")
    #设置一个变量，接受输入数据
    a=int(input("====================请输入您要执行的功能：=====================\n"))
    #如果等于菜单1：增加功能则列表list1接受的值
    if a == 1:
        list1[0]["姓名"]=input("请输入姓名：")
        list1[1]["性别"]=input("请输入性别：")
        list1[2]["出生日期"]=input("请输入出生日期：")
        list1[3]["班级"]=input("请输入班级：")
        list1[4]["学号"]=input("请输入学号：")
        #值传入列表后续把csv文件内容遍历上来，判断是否学号重复
        with open(r"D:\pythonzuoye\xygl.csv","r",encoding="utf-8",newline="") as f:
            a1=csv.reader(f)
            #遍历文件数据
            for i in  a1:
                #如果文件学号重复，退出循环
                if list1[4]["学号"]==str(i[4])[8:12]:
                    print("学号重复！请重新输入！！！")
                    break
                
                if list1[4]["学号"]!=str(i[4])[8:12]:
                    with open(r"D:\pythonzuoye\xygl.csv","a",encoding="utf-8",newline="") as f:
                            a1=csv.writer(f)
                            a1.writerow(list1)
               
                
            
                            
    
    elif a == 2:
        a2=input("请输入要更新学员姓名：")
        #需要遍历csv
        #把csv数据转成列表
        #拿列表做条件
        if list1[0]["姓名"]==a2:
            list1[0]["姓名"]=input("请输入姓名：")
            list1[1]["性别"]=input("请输入性别：")
            list1[2]["出生日期"]=input("请输入出生日期：")
            list1[3]["班级"]=input("请输入班级：")
            list1[4]["学号"]=input("请输入学号：")
            with open(r"D:\pythonzuoye\xygl.csv","a",encoding="utf-8",newline="") as f:
                a1=csv.writer(f)
                a1.writerow(list1)
        else:
            print("查无此人！！！")

        
        