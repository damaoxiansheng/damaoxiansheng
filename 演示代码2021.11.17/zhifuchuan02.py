"""
    字符串的输出：
        常见占位符：
        %d：整数占位符
        %f：浮点型数据占位符
        %s：字符串占位符
        %5d：占5个字符宽度，如果给的数据不足5个，就左侧补空，超出则不受宽度限制
        %5.4f：总长度为5（包括.）,小数部分精度为4，不足右侧补零
"""
age = 200
print("我的年龄是：%d"%20)
print("我的年龄是：%s"%"20")
print("我的年龄是：%s"%20)
print("我的年龄是：%s"%age)
print("我的年龄是：%5d"%age)

salary = 1234.23
str1 = "dfdgsgf"
print("我的年龄是：%d"%salary)
print("我的年龄是：%s"%salary)
print("我的年龄是：%9.3f"%salary)

print("我的年龄是："+str(age)+",正年轻！！")