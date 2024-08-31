# 无参数，无返回值
import random

def hello():
    print("Hello")

# 无参数，有返回值
def get_rand():
    return random.randint(0, 10)

# 有参数，无返回
def say_hi(name):
    print("你好, {}!".format(name))

# 有参，有返回
def sum(a, b):
    return a + b


hello()
print(get_rand())
say_hi("张三")
print(sum(3, 5))