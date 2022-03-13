import os
import sys
import time

from ggmk import rizhi

path = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
print(path)
sys.path.append(path)
time.sleep(4)
print(sys.path)

rizhi.rizhi("测试", "1234", "脚本执行成功1 ！")
