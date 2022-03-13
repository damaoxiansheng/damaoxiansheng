#作为单元测试的测试对象
class calculator():
    #实现加法运算
    def add(self,a,b):
        return a+b
    #实现减法运算
    def minus(self,a,b):
        return a-b
    #实现乘法运算
    def multi(self,a,b):
        return a*b
    #实现除法运算
    def devide(self,a,b):
        return a/b
    
    # 实现一个乘方的算法(该方法仅做完了设计，但是还没有实现具体的逻辑)
    # 这种方法需要设计用例，但是不需要执行该用例
    def chengfang(self,a):
        pass