name = "Hello PKG"

def say():
    print("Hello  PKG world")

class Nice:

    def __init__(self) -> None:
        self.name = "Hi Nice PKG"

# 直接运行hell->name
if __name__ == '__main__':
    pass

# 如果作为其他文件一个模块导入，__name__ : "hello"
