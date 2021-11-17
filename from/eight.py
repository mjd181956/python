"类和对象的碰撞"
from bs4 import BeautifulSoup
class Girl:
    #创建构造方法
    def __init__(self, name):
        self.name = name
    #创建普通方法，获取女生名字
    def get_name(self):
        return self.name
#创建两个对象
my_girl1=Girl("小妹")
my_girl2=Girl("晓丽")
#获得两个对象的名字
name1=my_girl1.get_name()
name2=my_girl2.get_name()
#打印结果
print("我有两个女盆友：","一个叫：",name1,",一个叫：",name2)



#创建一个人类
class person():
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    #维修电脑
    def repair_computer(self):
        print("我会维修电脑")
    #煮饭
    def cooking(self):
        print("我会煮饭")
#实例化对象
xiaoming=person("小明","男")
xiaoming.cooking()

class Cat():
    def __init__(self,name):
        self.name=name
    #成员函数
    def play(self):
        print(self.name+"在玩耍")
    #成员方法
    def sleep(self):
        print(self.name+"在睡觉")
#实例化对象，创建两个对象，并且每个对象名字不一样
co_Cat=Cat("卡菲猫")
sh_Cat=Cat("短毛猫")
#调用方法
co_Cat.play()
sh_Cat.sleep()
sh_Cat.play()



html="这是一个网页源码"
soup=BeautifulSoup(html,"lxml")
#使用对象的方法
soup.find_all("")

class Man:
    #类变量
    hand=2
    eye=2

    def __init__(self,name,age,sex):
        #成员变量
        self.__name=name
        self.age=age
    def lean(self):
        print(self.__name+"喜欢学习")
    def play(self):
        print(self.name+"喜欢玩耍")
xiaoming=Man("小明","6","男")
#print(xiaoming.name)
xiaoming.lean()
print(Man.eye)
print(xiaoming.eye)


#类方法
class Woman:
    #类方法
    @classmethod
    def showwinfo(cls):
        print("我是一个类方法")
    #成员方法
    def lean(self):
        print("我会学习")
#使用方法，第一种方式：类名.方法名
Woman.showwinfo()

#使用方法，第二种方式：对象名.方法名
xiaoming=Woman()
xiaoming.showwinfo()
xiaoming.lean()


"类与对象之间继承"
#父类
class Ancestors:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def blood(self):
        print("血脉之力")
#子类
class Descendant(Ancestors):
    pass

xiaoshu = Descendant("小书",10)
xiaoshu.blood()


"动物类"
# class Animal:
#     def __init__(self):
#         pass
#     def sleep(self):
#         print(self.name+"在睡觉")
# #猫科
# class Cat(Animal):
#     def __init__(self,name):
#         self.name = name
#     def sleep(self):
#         print("这只猫在睡觉")
#         super().sleep()
# cat=Cat("卡菲猫")
# cat.sleep()

#动物类
class Animal:
    def case(self):
        self.play()
#猫类
class Cat(Animal):
    def __init__(self,name):
        self.name = name
    def play(self):
        print(self.name+"在玩耍")
#狗类
class Dog(Animal):
    def __init__(self,name):
        self.name =name
    def play(self):
        print(self.name+"在玩耍")
cat =Cat("卡菲猫")
dog=Dog("二哈")
cat.case()
dog.case()

#计算公式类
class Count:
    def __init__(self):
        pass
    def add(self,num1,num2):
        result=num1+num2
        return result
    def minus(self,num1,num2):
        result=num1-num2
        return result
    def multiply(self,num1,num2):
        result=num1*num2
        return result
    def devide(self,num1,num2):
        result=num1/num2
        return result
class Calc(Count):
    def __init__(self,name,volume,electricity):
        self.name = name
        self.__volume=volume
        self.__electricity=electricity
    def show_volu(self):
        print("当前音量为："+self.__volume)
    def show_elec(self):
        print("当前电量为："+self.__electricity)
    def divide(self,num1,num2):
        if num2==0:
            return ""
        else:
            result=num1//num2
            return result
calc=Calc("XX品牌","100","50")
data=calc.add(2,5)
data2=calc.divide(6,3)
calc.show_elec()
print("2+5等于",data)
print("6/3=",data2)

        






         