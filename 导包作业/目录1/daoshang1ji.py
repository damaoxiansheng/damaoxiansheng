#导入上级目录中的模块
import  os
import sys
a1=os.path.abspath(os.path.dirname(__file__))
a2=os.path.abspath(os.path.dirname(a1))
sys.path.append("d:\pythonzuoye\导包作业")
print(sys.path)
import lx
#导入下级目录中的模块
import 目录1.目录3.lx2
#导入同级目录下的模块
import 目录2.lx3
#导入同级目录子目录下的模块
import 目录2.测试2.lx4