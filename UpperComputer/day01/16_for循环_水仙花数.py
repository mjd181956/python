# 打印出所有"水仙花数"，所谓"水仙花数"是指一个三位数[100, 1000)，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
for num in range(100, 1000):
    baiwei = num // 100
    shiwei = num // 10 % 10
    gewei = num % 10
    if (baiwei ** 3 + shiwei ** 3 + gewei ** 3 == num):
        print("{} + {} + {} = {}".format(baiwei ** 3, shiwei ** 3, gewei ** 3, num))
