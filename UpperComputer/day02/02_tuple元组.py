names = ("柯南", "小五郎", "毛利兰")
print(names, type(names))

# 自动组包 tuple
name = "柯南", "毛利兰"
print(name, type(name))

stu = "张干饭", 26, 175.5
name, age, height = stu
print("name: {}, age: {}, height: {}".format(name, age, height))

print("-------------------------数据交换")
a = 4
b = 5
temp = a
a = b
b = temp
print(a, b)

a = 3
b = 2
b, a = a, b
print(a, b)

print("------------------------内容不可修改")
names = ("柯南", "小五郎", "毛利兰")
new_names = list(names)
new_names.append("柯南2")
print(new_names)

Actor = ["袁鹏飞", "罗永浩", "俞敏洪", "李永乐", "王芳芳", "马云", "马化腾", "李彦宏"]
Actor_tuple = tuple(Actor)
