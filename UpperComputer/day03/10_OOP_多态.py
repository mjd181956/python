class Human:
    def eat(self):
        print("人类吃饭")

# 中国人
class ZhHuman(Human):
    def eat(self):
        print("中国人用筷子吃饭")

# 美国人
class USHuman(Human):
    def eat(self):
        print("美国人用刀叉吃饭")

#印度人
class IndiaHuman(Human):
    def eat(self):
        print("印度人手抓吃饭")

#函数
def someone_eat(someone: Human):
    """接收一个具备eat方法的对象

    :param someone: 对象
    """
    someone.eat()


# 创建对象
human = Human()
zh_man = ZhHuman()
us_man = USHuman()
in_man = IndiaHuman()

someone_eat(human)
someone_eat(zh_man)
someone_eat(us_man)
someone_eat(in_man)
