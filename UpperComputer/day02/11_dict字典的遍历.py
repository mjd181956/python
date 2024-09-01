ages = {
    "Tom": 18,
    "Jerry": 22,
    "Spike": 27,
    "Jack": 17
}
# 直接遍历
for key in ages:
    print(key, ages[key])

print("-------------------------")

for key in ages.keys():
    print(key, ages[key])

print("-------------------------")
#获取所有value,遍历
for value in ages.values():
    print(value)

print("-------------------------")
# 获取所有键值对
for item in ages.items():
    print(item, type(item))