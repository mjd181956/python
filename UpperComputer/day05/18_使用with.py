lst = [
    "今天天气不错",
    "挺风和日丽的",
    "我们下午在上课",
]
with open("c.txt", "w+", encoding = "utf-8") as f:
    # 通过推导式，给每个元素追加一个\n
    lst = [item + '\n' for item in lst]

    f.writelines(lst)
    f.seek(0)  # 跳到指定字节
    
    content = f.read()
    print(content)
    
print("closed: ", f.closed)