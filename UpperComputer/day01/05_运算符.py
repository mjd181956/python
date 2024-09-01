a = 5
b = 2
# ---------赋值运算符
a += b
print(a)    # 7

a *= b
print(a)  # 14

a /= b
print(a)  # 7.0

a //= b
print(a)  # 3.0

print(a % 2)

a = 5
b = 2
a **= b
print(a)  # 25.0

print("------------------------------------比较运算符")

a = 5
b = 2
print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a < b)  # False

print("------------------------------------逻辑运算符")

print(" True and False: ", True and False)  # False
print(" True and True: ", True and True)  # True

print(" True or False: ", True or False)  # True
print(" False or False: ", False or False)  # False

print("not True: ", not True)  # False
