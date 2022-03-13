'''
    该文件负责测试计算器类中加法运算功能。
    设计单元测试用例：
'''
# 1、导包
import unittest
from jisuanqi import mathdemo

# 2、下面是固定的格式，创建一个类，继承自unittest的testcase的类
# 这个类可以叫做测试用例类
# 类名可以和文件名一致
class testAdd(unittest.TestCase):

    # 资源初始化方法，名字是固定的
    def setUp(self):
        print("我是setUp方法")
        # 先创建一个calculator对象
        self.calc = mathdemo()


    # 测试用例的方法，test开头，其后的（数字、字母、下划线）
    def test_add_01(self):
        print("我是test_add_01方法")
        # 获取实际结果了
        actualValue = self.calc.add(1,2)
        expectValue = 3
        # 断言
        # assertEqual (first: Any, second: Any, msg: Any = ...)
        self.assertEqual(actualValue,expectValue,"预期和实际结果是不一致的")



    # 资源释放方法，名字也是固定的
    def tearDown(self):
        print("我是tearDown方法")



if __name__ == "__main__":
    # 调用unittest的main方法来执行单元测试用例类中的所有测试用例
    unittest.main()
