def caidan():
    b=["张三"]
    while True:
        a=[1,2,3,4,5]
        print("====================学员管理菜单====================\n%s-增加新学员 %s-更新  %s-删除学员  %s-查询  %s-退出\n===================================================="%(a[0],a[1],a[2],a[3],a[4]))
        zj=int(input("请选择一个菜单项（输入1~5的数字）:"))
        if zj==a[0]:
            b.append(input("请输入新增学员姓名："))
            print(b[:])
        elif zj==a[1]:
            b.remove(input("请输入已有的姓名："))
            b.append(input("请输入改为的姓名："))
            print(b[:])
        elif zj==a[2]:
            b.remove(input("请输入要删除的姓名："))
            print(b[:])
        elif zj==a[3]:
            print(b[:])
        elif zj==a[4]:
            break
        else:
            print("请输入正确菜单项！！")
