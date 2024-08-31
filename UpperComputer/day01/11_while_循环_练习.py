"""根据用户输入的数值n,打印n行三角形"""

count = int(input("请输入行数: "))

# 正三角形
# row = 1
# while row <= count:
#     print("*" * row)
#     row += 1

row = count
while row >= 1:
    print("*" * row)
    row -= 1