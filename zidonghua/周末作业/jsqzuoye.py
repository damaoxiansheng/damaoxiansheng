#导入计算器方法
from unittest.main import main
from unittest.result import TestResult
from unittest.suite import TestSuite
from jisuanqi import jisuanqi
#导入unitest框架
import unittest

#创建一个测试用例类
class jsqzuoye(unittest.TestCase):
    
    #写入unittest固定格式
    def setUp(self):
        #使一个对象等于此方法
        self.dx = jisuanqi()
        
    #创建一个加法运算用例
    def test_jia_001(self):
        """加法运算用例"""
        js = self.dx.jia(1,2)
        #预期结果等于
        yq = 3
        #创建一个断言
        self.assertEqual(js,yq,"预期结果与实际结果不符！！")
        
    #创建一个减法运算用例
    def test_jian_002(self):
        """减法运算用例"""
        sj = self.dx.jian(3,1)
        yq = 2
        #断言
        self.assertEqual(sj,yq,"预期结果与实际结果不符！！！")
    
    
    #创建一个乘法的运算用例
    def test_chen_003(self):
        """乘法的运算用例"""
        sj = self.dx.chen(2,2)
        yq = 4
        #断言
        self.assertEqual(sj,yq,"预期结果与实际结果不符！！！")
        
    #创建一个除法的测试用例
    def test_chu_004(self):
        """除法的测试用例"""
        sj = self.dx.chu(4,2)
        yq = 2
        #断言
        self.assertEqual(sj,yq,"预期与实际结果不符！！！")
    
    def tearDown(self):
        pass

#创建一个用例集合
yljh = TestSuite()

#添加用例到此集合
yljh.addTest(jsqzuoye("test_jia_001"))
yljh.addTest(jsqzuoye("test_jian_002"))
yljh.addTest(jsqzuoye("test_chen_003"))
yljh.addTest(jsqzuoye("test_chu_004"))

#打印一手用例集合
print(yljh)

#创建一个对象保存运行结果
jg = TestResult()

#运行集合用例，结果保存到TestResult对象
yljh.run(jg)

#打印运行结果
print(jg.__dict__)