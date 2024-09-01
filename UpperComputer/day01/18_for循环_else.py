for i in range(10):
    if i == 3:
        break
    print("媳妇我错了", i)
else:
    print("顺利完成，原谅我了")
print("----------------------------------------")

for i in range(10):
    if i % 2 == 0:
        continue
    print("媳妇我错了", i)
else:
    print("顺利完成，原谅我了")