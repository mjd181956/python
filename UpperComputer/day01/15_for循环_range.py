r = range(10)
print(r, type(r))

lst = list(range(10))
print(lst, type(lst))

# [start,stop) step
for i in range(10):
    print(i, end=" ")

print()
for i in range(2, 10, 2):
    print(i, end=" ")

print()

for i in range(10, 0, -1):
    print(i, end=" ")
