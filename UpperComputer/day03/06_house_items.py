# ----------------------------------------Item 家具类
class Item:
    def __init__(self, name, area):
        """家具类的初始化方法

        :param name: 家具的名称
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return f"str家具名称: {self.name}, 占地面积: {self.area}"

    def __repr__(self):
        return f"repr家具名称: {self.name}, 占地面积: {self.area}"

# -----------------------------------------House 房子类


class House:
    def __init__(self, address, area):
        """房子的初始化方法

        :param address: 房子地址
        :param area: 套内面积
        """
        self.address = address
        self.area = area
        # 剩余面积
        self.free_area = self.area
        # 家具列表
        self.items = []

    def add_item(self, item):
        """添加家具方法

        :param item: 家具对象
        """
        if self.free_area >= item.area:
            self.items.append(item)
            self.free_area -= item.area
        else:
            print("面积不足，无法添加")

    def __str__(self) -> str:
        return f"房子地址: {self.address}, 套内面积: {self.area}, 剩余面积: {self.free_area}"


# 1. 创建 家具对象, 输出 家具信息
item1 = Item("沙发", 20)
item2 = Item("餐桌套装", 40)
item3 = Item("家庭影院", 80)
print(item1)
print(item2)
# 2. 创建 房子对象, 输出 房子信息
house = House("北京市石景山区", 120)
print(house)
# 3. 房子添加家具, 输出 房子信息
house.add_item(item1)
house.add_item(item2)
print(house, "家具数量：", len(house.items))
print(house.items)
