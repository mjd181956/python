"""
计算n的阶乘

5 * 4 * 3 * 2 * 1
"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


