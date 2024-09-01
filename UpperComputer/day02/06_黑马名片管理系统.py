"""
1. 程序启动，显示名片管理系统欢迎界面，并显示功能菜单
2. 用户用数字选择不同的功能：新建名片、显示名片、查询名片、退出系统
  a. 用户名片需要记录用户的 姓名、电话、QQ、邮件
  b. 显示名片可以列举出所有已经保存的名片
  c. 如果查询到指定的名片，用户可以选择 修改、删除 名片
"""

main_tip = """**************************************************
欢迎使用[名片管理系统] V1.0

1. 新建名片
2. 显示名片
3. 查询名片

0. 退出系统

**************************************************
"""
card_list = [
    ["张锋", 1232312312, 12345466, "123@qq.com"]
]

def create_card():
    """新建名片，并加入cards列表中
    """
    print("新建名片")
    names = input("请输入姓名：")
    phone = int(input("请输入电话号码："))
    qq = int(input("请输入qq号："))
    email = input("请输入电子邮箱：")
    card = [names, phone, qq, email]
    card_list.append(card)
    print("添加【{}】名片成功".format(names))


def show_card():
    """显示所有名片
    """
    print("显示名片")
    for card in card_list:
        print(card)

def card_handle(card):
    """修改、删除名片
    """

    print("修改、删除名片")
    while True:
        action = input("请选择操作：1.修改 2.删除 0.返回：")
        if action == "1":   # 修改
            print("修改名片")
            # modify_card(card)
        elif action == "2":  # 删除
            print("删除名片")
        elif action == "0":
            break
        else:
            print("输入有误，请重新输入！")


def search_card():
    """根据用户输入的姓名进行匹配第一个查询的值
    """
    print("查询名片")
    query_name = input("请输入要查询的姓名：")
    for card in card_list:
        if query_name == card[0]:
            print("找到了 ", card)
            card_handle(card)
            return
    else:
        print("没有找到【{}】名片".format(query_name))


while True:
    print(main_tip)

    action = input("请选择功能：")

    if action == "1":
        # print("新建名片")
        create_card()
    elif action == "2":
        # print("显示名片")
        show_card()
    elif action == "3":
        # print("查询名片")
        search_card()
    elif action == "0":
        print("退出系统")
        exit(0)
    else:
        print("输入有误，请重新输入！")

# def show_menu():
#     print("*" * 50)
#     print("欢迎使用[名片管理系统] V1.0")
#     print("")
#     print("1. 新建名片")
#     print("2. 显示名片")
#     print("3. 查询名片")
#     print("")
#     print("0. 退出系统")
#     print()
#     print("*" * 50)
# show_menu()
