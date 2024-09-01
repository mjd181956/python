# 1.打开文件
f = open("a.txt", encoding="utf-8")
# 2.读取文件内容
content = f.read(5)
print(content)

line = f.readline()
print(line)

lines = f.readlines()
print(lines)

# 3.关闭文件
f.close()