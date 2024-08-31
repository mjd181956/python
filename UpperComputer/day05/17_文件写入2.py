lst = [
    "今天天气不错",
    "挺风和日丽的",
    "我们下午在上课",
]
try:
    # 使用with 可以保证即使出现异常，可以关闭文件
    with open("c.txt", "w", encoding = "utf-8") as f:

        # 通过推导式，给每个元素追加一个\n
        lst = [item + '\n' for item in lst]

        f.writelines(lst)
        a = 3 / 0
        f.close()
except:
    pass

print("closed: ", f.closed)