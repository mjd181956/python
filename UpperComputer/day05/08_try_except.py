a = 10
b = 0
try:
    c = a / b
    print("结果", c)
    
except ZeroDivisionError:
    print("除数不能为0")