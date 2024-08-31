# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("%d * %d = %d" % (col, row, row * col), end="\t")
#         col += 1
#     print()
#     row += 1

row = 9
while row >= 1:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, row * col), end="\t")
        col += 1
    print()
    row -= 1