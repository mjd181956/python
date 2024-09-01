"""
超市买苹果计算金额
需求 :
●  收银员输入苹果的价格price，单位：元/斤
●  收银员输入用户购买苹果的重量weight，单位：斤
●   计算并输出付款金额:xxx元
"""

pice = input("请输入苹果的单价：")
weight = input("请输入苹果的重量：")
pice = float(pice)
weight = float(weight)

print("付款金额：%0.2f" % (pice * weight))
