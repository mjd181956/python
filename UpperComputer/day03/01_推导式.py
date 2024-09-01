"""
推导式指的是轻量级循环创建数据的方式，对列表或可迭代对象中的每个元素应用某种操作，用生成的结果创建新的列表；或用满足特定条件的元素创建子序列。
推导式包括：
● 列表推导式
● 元组推导式
● 集合推导式
● 字典推导式

"""
# ● 列表推导式(0~10所有偶数的平方的列表)
lst = [i for i in range(10)]
lst = [i ** 2 for i in range(10)]
lst = [i ** 2 for i in range(10) if i % 2 == 0]
print(lst)

# ● 元组推导式 <genexpr> 可迭代对象
tup = (i ** 2 for i in range(10) if i % 2 == 0)
print(tuple(tup))
# for ele in tup:
#     print(ele)

# ● 集合推导式
ss = {i ** 2 for i in range(10) if i % 2 == 0}
print(ss, type(ss))

# ● 字典推导式

_dict = {key: key ** 2 for key in range(10) if key % 2 == 0}
print(_dict, type(dict))

lst1 = [0, 1, 2]
lst2 = ["张三", "李四", "王五"]
print(list(zip(lst1, lst2)))
_dict2 = {k: v for k, v in zip(lst1, lst2)}
print(_dict2)
