lst = [
    "今天天气不错",
    "挺风和日丽的",
    "我们下午在上课",
]
f = open("c.txt", "a+", encoding = "utf-8")

# 通过推导式，给每个元素追加一个\n
lst = [item + '\n' for item in lst]

f.writelines(lst)

a = 3 / 0

f.close()