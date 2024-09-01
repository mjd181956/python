def read_file():
    
    a = 10
    b = 0
    
    try:
        rst = a / b
        print("结果：", rst)
        
        print("计算之后，代码正常运行")
        return rst
    except ZeroDivisionError:
        print("除数不能为0")
    finally:
        print("finllay 关闭资源，无论是否有异常，都会执行")
        
"""
try-except
try-finally
try-except-finally
"""
def write_file():
    f = open("haha.txt", "w")
    try:
        f.write("abc")
    except Exception as e:
        print("出现异常", e, type(e))
    finally:
        f.close()
        print("关闭资源")    
    
        
if __name__ == '__main__':
    read_file()
    write_file()