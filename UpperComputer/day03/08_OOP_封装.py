class WashMachine:

    def __init__(self, brand, capacity):
        """洗衣机的初始化函数

        :param brand: 品牌
        :param capacity: 容量
        """
        self.brand = brand
        self.capacity = capacity
        # 门状态
        self.is_close = False
        # 模式：0：未设定模式，1：轻柔模式，2：狂揉模式
        self.__mode__ = 0
        # 转速
        self.__motor_speed = 0

    def open_door(self):
        print("打开洗衣机门")
        self.is_close = False

    def close_door(self):
        print("关闭洗衣机门")
        self.is_close = True

    def set_mode(self, mode):
        if mode == 1:
            print("设置轻柔模式")
            self.__mode__ = 1
        elif mode == 2:
            print("设置狂揉模式")
            self.__mode__ = 2
        else:
            print("未设定模式")

    def wash(self):
        if not self.is_close:
            print("请关闭洗衣机门，哔哔哔...")
            return
        if self.__mode__ == 0:
            print("请先设置洗衣模式")
            return
        print("放水 ...")
        print("放满了...")
        if self.__mode__ == 1:
            print("轻柔模式，洗内衣")
            # 调节马达转速
            self.__motor_speed = 1000
            print("马达转速：", self.__motor_speed)
        elif self.__mode__ == 2:
            print("狂揉模式，洗大衣")
            # 调节马达转速
            self.__motor_speed = 2000
            print("马达转速：", self.__motor_speed)

        print("开始洗衣")
        print("洗衣结束")


# 创建对象
machine = WashMachine("海尔", 10)
machine.open_door()
machine.close_door()
machine.set_mode(1)
machine.wash()