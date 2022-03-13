'''
    逻辑运算符：(掌握布尔数据运算的处理)
        运算数可以是boolean类型，就比较简单，结果就是布尔类型。
        and：逻辑与运算
            x and y: 
                如果x是False，结果是False；否则结果就是y
            参与运算的布尔值：如果有False结果就是False，只有全True结果才为True
            True and True
            True and False
            False and True
            False and False

            如果参与运算的不仅仅是布尔值：
                如果and前的是True，结果就是and后的数据
                如果and前的是False，结果就是False
                如果and前的是数字，返回的and后的值
        
        or：或运算
            x or y：
                x是True，则结果就是True
                x是false，则返回的y的值
                x是非布尔，则结果就是x
        not: 非运算
            not True就是False
            not False就是True
'''
print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("==========================")
# 如果and前的是True，结果就是and后的数据
print(True and 2)
print(2 and False)
print(False and 2)
print(2 and True)
print("==========================")
print(True or False)
print(False or False)
print(False or True)
print(1 or True)
print("==========================")
print(not True)
print(not False)
print(not 2)
print(not 0)