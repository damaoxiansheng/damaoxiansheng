'''
    该文件负责测试计算器类中加法运算功能。
    设计单元测试用例：
'''
# 1、导包
import unittest
from calculator import calculator

# 2、下面是固定的格式，创建一个类，继承自unittest的testcase的类
# 这个类可以叫做测试用例类
# 类名可以和文件名一致
class testAdd_02(unittest.TestCase):

    # 资源初始化方法，名字是固定的
    def setUp(self):
        print("我是setUp方法")
        # 先创建一个calculator对象
        self.calc = calculator()


    # 测试用例的方法，test开头，其后的（数字、字母、下划线）
    def test_add_03(self):
        print("我是test_add_03方法")
        # 获取实际结果了
        actualValue = self.calc.add(2,2)
        expectValue = 3
        # 断言
        # assertEqual (first: Any, second: Any, msg: Any = ...)
        self.assertEqual(actualValue,expectValue,"预期和实际结果是不一致的")

    # 测试用例的方法，test开头，其后的（数字、字母、下划线）
    def test_add_04(self):
        print("我是test_add_04方法")
        # 获取实际结果了
        actualValue = self.calc.add(1,2)
        expectValue = 3
        # 断言
        # assertEqual (first: Any, second: Any, msg: Any = ...)
        # self.assertEqual(actualValue,expectValue,"预期和实际结果是不一致的")
        # flag = xxxxx.is_displayed()
        # self.assertTrue(flag)
        # str1 = "abcdef"
        # self.assertNotIn("ab",str1)
        # str1 = "abc"
        # self.assertIsInstance(str1,str)




    
    # skip: 跳过某条用例的执行，无条件跳过的方式
    @unittest.skip("改方法还没实现呢！！！，先别执行！！！")
    def test_chengfang_04(self):
        actualValue = self.calc.chengfang(2)
        expectValue = 4
        self.assertEqual(actualValue,expectValue,"预期和实际结果是不一致的")
    
    # skipI：有条件的跳过某条用例
    @unittest.skipIf(1==1,"符合条件就跳过")
    def test_chengfang_03(self):
        actualValue = self.calc.chengfang(2)
        expectValue = 4
        self.assertEqual(actualValue,expectValue,"预期和实际结果是不一致的")

    # 设计一条除法的用例,就是要测试这条用例数据报异常的
    # 这条用例一定要抛异常，否则报错
    @unittest.expectedFailure
    def test_chu_02(self):
        actualValue = self.calc.devide(4,0)
        expectValue = 2
        self.assertEqual(actualValue,expectValue,"预期和实际结果是不一致的")

    # 资源释放方法，名字也是固定的
    def tearDown(self):
        print("我是tearDown方法")
        self.calc = None

if __name__ == "__main__":
    # 调用unittest的main方法来执行单元测试用例类中的所有测试用例
    # main(): 入口方法，把所有的用例运行一遍
    # 能不能定制执行哪一些用例？
    # 能不能定制执行的顺序？
    unittest.main()

    # 测试集合的概念，来实现上面的两个问题（用例的管理）
    # 先创建一个测试集合的对象
    # suitt = unittest.TestSuite()
    # # print(suitt)
    # # addTest(): 追加一条测试用例到测试集合中
    # suitt.addTest(testAdd("test_add_02"))
    # suitt.addTest(testAdd("test_add_01"))
    # suitt.addTest(testAdd("test_chengfang_01"))
    # suitt.addTest(testAdd("test_chengfang_02"))
    # suitt.addTest(testAdd("test_chu_01"))
    # # 输出suitt
    # # print(suitt)
    # # 执行用例，测试集合（TestSuite）自带的运行功能-run()
    # # 先创建一个测试结果对象（TestResult），来存储测试结果的数据
    # result = unittest.TestResult()
    # # 集合运行（集合中用例运行）完成之后，把执行数据写入到result中
    # suitt.run(result)
    # # 查看结果对象中的数据
    # # <unittest.result.TestResult run=2 errors=0 failures=1>
    # # __dict__: 将测试执行的结果以字典的形式输出出来
    # print(result.__dict__)



