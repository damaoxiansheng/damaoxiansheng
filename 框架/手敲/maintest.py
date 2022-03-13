'''
    主运行文件：
        该文件的功能就是解决大量用例执行的问题的。
        代码后面需要持续改进（现在先写一个基本的）

    需求：
        要执行test_add_02.py和test_add.py中的测试用例。

'''
import  unittest
from HTMLTestRunner import HTMLTestRunner
# TestLoader：辅助将不同模块中的测试用例（在单元测试用例类中定义的test开头的那些方法）
# discover(start_dir,pattern)方法：把指定路径下的匹配到的测试用例返回给一个测试集合对象
# start_dir:是测试用例的模块所在的路径。./day05/
# pattern: 是匹配模式，"test*.py"

discover = unittest.defaultTestLoader.discover(r"框架\手敲",pattern="test*.py")
print(discover)
# TestRunner: 用于测试集合的
# TextTestRunner：是unitest自己的运行，文本运行
with open(r"./day05/result.txt","w",encoding="utf-8") as f:
    runner = unittest.TextTestRunner(f,descriptions=True,verbosity=3)
    runner.run(discover)


# # HTMLTestRunner：第三方运行器，是HTML格式的报告
with open(r"./day05/result.html","wb") as f:
    runner = HTMLTestRunner(f,title="测试报告",description="第一次执行的结果报告")
    runner.run(discover)