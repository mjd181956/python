"""
1. 声明Person类（class)

2. 根据Person类创建对象的Object（可以创建多个）

3. 调用对象的方法，获取属性
"""

# 声明类


class Person:

    # 初始化函数/构造函数
    def __init__(self, name, age):
        """构造函数
        self (自己) 不能少，代表当前创建的对象
        :param name: 姓名
        :param age: 年龄
        """
        self.name = name
        self.age = age

    def eat(self):
        print("吃饭")

    def run(self):
        print(self.name + "跑步")

    def say_hell(self, target):
        print(self.name + "对" + target + "说你好")


# 创建对象
p = Person("桑尼", 3)
print(p.name)
print(p.age)
p.eat()
p.run()

p2 = Person("小红", 2)
p2.run()
p2.say_hell("小芳")
