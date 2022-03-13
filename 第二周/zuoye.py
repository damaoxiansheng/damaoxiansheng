# 作业一
class Number():
    def __init__(self, n1, n2):
        self.__a = n1
        self.__b = n2

    def jia(self):
        return self.__a+self.__b

    def jian(self):
        return self.__a-self.__b

    def cheng(self):
        return self.__a*self.__b

    def chu(self):
        return self.__a/self.__b

sc = Number(9, 3)
print(sc.jia())
print(sc.jian())
print(sc.cheng())
print(sc.chu())


# 作业三
class Student ():
    def __init__(self, sNO, sName, sSex, sAge, sJava):
        self.xh = sNO
        self.xm = sName
        self.xb = sSex
        self.nl = sAge
        self.cj = sJava

    def getNo(self):
        return self.xh

    def getName(self):
        return self.xm

    def getSex(self):
        return self.xb

    def getAge(self):
        return self.nl

    def getJava(self):
        return self.cj

    def a(self):
        return {"学号": self.xh, "姓名": self.xm, "性别": self.xb, "年龄": self.nl, "成绩": self.cj}


a = Student("11111", "张三", "男", 19, 80)
b = Student("11112", "李四", "女", 19, 59)
c = Student("11113", "王五", "男", 19, 63)
d = Student("11114", "赵其", "男", 19, 42)
e = Student("11115", "刘霸气", "女", 19, 88)
print(a.a())
print(b.a())
print(c.a())
print(d.a())
print(e.a())
list1 = []
list1.append(a.getJava())
list1.append(b.getJava())
list1.append(c.getJava())
list1.append(d.getJava())
list1.append(e.getJava())
print("成绩最小是:%s" % (min(list1)))
print("成绩最大是:%s" % (max(list1)))
d1 = 0
for i in list1:
    d1 = d1+i
print("平均成绩是:%s" % (d1/len(list1)))
