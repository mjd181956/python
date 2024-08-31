g = 123
def func_a():
    a = 10

#声明后面用到的变量g为全局变量, 如果g不存在，会自动创建
    global g
    print("a = ", a)
    print("g = ", g)

def func_b():
    a = 20
    print("a = ", a)


func_a()
func_b()