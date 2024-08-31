"""可变长度参数"""

""" '*' 表示把一堆的参数传进去 """
def sum_nums(*args):
    print("args: ",type(args))
    rst = 0
    for i in args:
        rst += i
    return rst

if __name__ == '__main__':
    rst = sum_nums(1, 2, 3, 4)
    print(rst)
