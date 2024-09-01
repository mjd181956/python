ages = {
    "Tom": 18,
    "Jerry": 22,
    "Spike": 27,
    "Jack": 17
}
print(ages, type(ages))

#添加
ages["张三"] = 33
ages.setdefault("李四", 14)

# 移除
ages.pop("Jack")
del ages["Tom"]  # python2.0+使用的删除

# 修改
ages["Jerry"] = 23

print(ages)
