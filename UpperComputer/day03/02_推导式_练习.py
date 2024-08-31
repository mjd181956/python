"""
请写出一段 Python 代码实现分组一个 list 里面的元素
比如 [1,2,3,...100] 变成 [[1,2,3],[4,5,6]....[100]]
"""
lst = [10, 20, 30, 40, 50, 60, 70, 80]

lst = [i for i in range(1, 101)]
# rst = [i for i in range(len(lst)) if i % 3 == 0]
rst = [lst[i:i + 3] for i in range(len(lst)) if i % 3 == 0]
print(rst)
