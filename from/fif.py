a=(110,22.33,"tom")
b=110,22.33,"tom"
print(a)
print(b)

c=tuple("abcdef")
print(c)

tuple=(220,4,201,401)
print(tuple[0])
print(tuple[3])
print(tuple[-1])

for i in tuple:
    if 201 == i:
        print("存在")
        break

print(len(tuple))

print(max(tuple))

print(min(tuple))

list1=[1,2,3,8,20,13]
print(list1)
'print(tuple(list1))'




