"""
打印名片
"""
name = input("请输入姓名：")
company = input("请输入公司名称：")
title = input("请输入职位：")
telephone = input("请输入电话号码：")
email = input("请输入邮箱地址：")

print("*"*30)
print(company)
print()
print("%s(%s)" % (name, title))  # 如果字符串里有多个占位符，%后就写对应个数参数（）包括
print()
print("电话：%s" % telephone)
print("邮箱：%s" % email)
print("*"*30)
