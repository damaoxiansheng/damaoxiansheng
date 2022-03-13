'''
    已知列表 L = ['apple','pear','banana','oranger','grape']
    (1) 往列表L中追加“peach”
    (2) 定义另外一个列表L1 = [1,2,"A","B"],将该列表追加至L中
    (3) 向列表L开头添加“fruit:”
    (4) 获取列表L的总长度
    (5) 删除列表L的最后一个元素（使用两种方法）
    (6) 删除列表的第5个元素
    (7) 删除元素“A”

    已知列表 L2 = [2,1,4,5,4]
    (1)对列表L2进行排序--sort()
    (2)获取列表中的最大值和最小值
    (3)对排序好的列表进行逆序排列（使用两种方法）

'''
L = ['apple','pear','banana','oranger','grape']
# (1) 往列表L中追加“peach”
L.append("peach")
print(L)
# (2) 定义另外一个列表L1 = [1,2,"A","B"],将该列表追加至L中
L1 = [1,2,"A","B"]
# L.append(L1)
# L.extend(L1)
L.insert(0,L1)
# print(L)
# (3) 向列表L开头添加“fruit:”
L.insert(0,"fruit:")
print(L)
# (4) 获取列表L的总长度
print(len(L))
# (5) 删除列表L的最后一个元素（使用两种方法）
# L.pop()
del L[-1]
print(L)
# (6) 删除列表的第5个元素
del L[4]
print(L)
# (7) 删除元素“A”
del L[1][2]
print(L)

# 已知列表 L2 = [2,1,4,5,4]
L2 = [2,1,4,5,4]
# (1)对列表L2进行排序--sort()
L2.sort()
print(L2)
# (2)获取列表中的最大值和最小值
print(min(L2))
print(max(L2))
# (3)对排序好的列表进行逆序排列（使用两种方法）
# L2.reverse()
print(L2[::-1])