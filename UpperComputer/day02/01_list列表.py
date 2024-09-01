# 列表初始化
name_list = ["樱木花道", "卡卡西", "佐助", "纲手", '柯南', '自来也']
print(name_list)

# 追加
name_list.append("小兰")
print(name_list)

# 删除
name_list.remove("佐助")
print(name_list)

print(name_list)
print(name_list.pop(2))
print(name_list)

# 修改
print(name_list)
name_list[2] = "索隆"

# 查询
print("-----------------------------列表查询")
print(name_list[3])
print(name_list.index("小兰"))
print("------------------------------")
for name in name_list:
    print(name)

print("-----------------------------列表排序")

lst = [2, 5, 1, 3, 22, 12]
lst.sort()  # 排序
print(lst)

lst.sort(reverse=True)  # 倒叙
print(lst)

print("-----------------------------列表嵌套")
students = [
    ["樱木花道", 18, "男"],
    ["江流儿", 17, "女"],
    ["大蛇丸", 19, "男"]
]
print(students)
print(students[0][2])

