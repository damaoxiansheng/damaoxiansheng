#定义一个Vehicles类
class Vehicles():
     
    def __init__(self,name,color,weight,plate):
        self.name=name
        self.color=color
        self.weight=weight
        self.plate=plate
    
    def getDetails(self):
        return self.name,self.color,self.weight,self.plate
#定义一个子类Car
class Car(Vehicles):
    
    def __init__(self, name, color, weight, plate,seats,speed):
        Vehicles.__init__(self,name, color, weight, plate)
        self.__seats=seats
        self.speed=speed
    
    def get_seats(self):
        return self.__seats
    
    def set_seats(self,seats):
        self.__seats=seats
    
    def getDetails(self):
        return self.name,self.color,self.weight,self.plate,self.__seats,self.speed

    def speedUp(self,speed):
        if speed<200:
            self.speed=self.speed+speed
            return self.speed
        else:
            return "速度已经超过200！注意安全"
    
    def slowDown(self,speed):
        if speed>0:
            self.speed=self.speed-speed
            return self.speed
        else:
            return "速度小于0，你和我闹呢？？"
      
c1=Car("捷达","白色","1吨","京123","6座",60)
c2=Car("马自达","红色","2吨","京124","5座",150)
c3=Car("劳斯莱斯","黑色","5吨","京111","5座",200)
print(c1.speedUp(201))
print(c1.slowDown(0))

print(c1.getDetails())
print(c2.getDetails())
print(c3.getDetails())

#第二大题
class Door():
    def __init__(self,height):
        self.height=height
    
    def set_height(self,height):
        self.height=height
    
    def get_height(self):
        return self.height
    
    def opendoor(self,doorName):
        print("打开doorName")

class MyDoor(Door):
    def __init__(self,height,doorName):
        super().__init__(height)
        self.height=height
        self.doorName=doorName
    
    def opendoor(self):
        print("打开%s"%self.doorName)

myDoor = MyDoor("MyDoor",123)
myDoor.opendoor()
myDoor = MyDoor(2.1,"盼盼")
myDoor.doorName = "aa"
myDoor.opendoor() 