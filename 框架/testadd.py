"""
    该文件负责测试计算器类中加法运算 功能
    设计单元测试用例
"""
#导包
import unittest
from unittest.main import main
from jisuanqi import mathdemo

class testadd(unittest.TestCase):
    
    def setUp(self):
        self.a1 = mathdemo()
        
    
    def test_add(self):
        yq = mathdemo.add(1,2)
        sj = 3
        self.assertEqual("yq","sj","用例执行成功！！！")
        
    
    def tearDown(self):
        pass
        print('==================')    

if __name__ == "__main__" :
    unittest.main()