# -----------------------------------------定义Person类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}"

    def sya_hell(self):
        print(f"{self.name}说:你好")

# -----------------------------------------定义Student类继承了Person类
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)  # 调用父类的初始化方式
        # 定义自己的属性
        self.score = score

    def play(self):
        print(f"{self.name}打游戏")


#创建学生
stu = Student("小明", 17, 99.5)
print(stu)

#访问父类方法
stu.sya_hell()
