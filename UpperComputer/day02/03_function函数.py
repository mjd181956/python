"""
打招呼函数
"""


def say_hello():
    print("hello World!")
    print("hello World!")
    print("hello World!")


say_hello()


def sum(a, b):
    """求两个数之和

    :param a: 参数1
    :param b: 参数2
    :return: 参数1与参数2之和
    """
    return a + b


def max(a, b):
    """返回两个数较大那个

    :param a: 参数1
    :param b: 参数2
    :return: 较大值
    """
    if a > b:
        return a
    else:
        return b


def cal(a, b):
    """计算连个数的乘积和商

    :param a: 参数1
    :param b: 参数2
    :return: 乘积和商
    """
    # 两个数的乘积
    multipy = a * b
    if (b == 0):
        return multipy, None
    divide = a / b
    return multipy, divide


print(sum(1, 2))
print(max(21, 32))

print(cal(2, 3))
print(cal(2, 5))