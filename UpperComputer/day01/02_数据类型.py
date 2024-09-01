"""
变量定义，基本数据类型
"""

# 字符串类型
name = "张三"

# 整数类型
age = 18

# 浮点类型
height = 180.5

# 布尔类型
handsome = True

# 复数
compl = 3 + 4j

print("height:", height, " age ", age)
print(type(name))
print(type(age))
print(type(height))

# ------------------------------------

""" 非法变量名
1. 只能由字母、数字、下划线
2. 不能以数字开头
3. 不能使用关键字
4. 区分大小写
"""

user_name = "zhang"
userName = "san"
USERNAME = "feng"
print(user_name, userName, USERNAME, "\n")

print("---------------------------------")

a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # 得到float
print(a//b)  # 得到int
print(a % b)  # 取模
print(a**b)  # a^b a的b次幂

print("------------------------------------")

pwd = "abc123"
# 字符串直接通过+拼接
print(user_name+pwd)

# 字符串可以和数字相乘，重复a次
print(user_name*3)
