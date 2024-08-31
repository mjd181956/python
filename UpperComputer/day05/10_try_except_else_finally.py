a = 10
b = 1

try:
    result = a / b
    print(f"1.result: {result}")
except:
    print("2.除数不能为0")
else:
    print("3.没有异常")
finally:
    print("4.最终执行的代码")