class lx():
    
    def __init__(self,name,age,sex,cs):
        self.name=name
        self.__age=age
        self.sex=sex
        self.__cs=cs
    
    
    def gb_cs(self):
        return self.__cs
    
    def xg_age(self,age):
        if 90>age>0:
            self.__age=age
            return self.__age
        else:
            return "请输入正确年龄"
    

yihao=lx("张云辉",18,"女","宣化")

print(yihao.gb_cs())
print(yihao.xg_age(19))

class lx2(lx):
    
    def __init__(self,name,age,sex,cs,aihao):
        self.aihao=aihao
        super().__init__(name,age,sex,cs)
    
    def ckxb(self):
        return self.sex
    
    def ah(self):
        return self.aihao
    
class lx3(lx2):
    
    def __init__(self,name,age,sex,cs,aihao,shujiao):
        self.shujiao=shujiao
        lx2.__init__(self,name,age,sex,cs,aihao)

    def ah(self):
        print("喜欢溜爷爷")
    
    def sj(self):
        print("喜欢睡大觉")
        
        
ren1 = lx2("张云辉",16,"女","张家口","吹牛逼")

print(ren1.ckxb()) 
print(ren1.ah())

ren3=lx3("张云辉",16,"女","张家口","遛鸟","打呼噜")
ren3.ah()
print(ren3.gb_cs())
print(ren3.xg_age(20))
ren3.ah()
ren3.sj()