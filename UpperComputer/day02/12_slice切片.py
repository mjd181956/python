"""
取一个str、list、tuple的部分元素是非常常见的操作
● 切片 译自英文单词slice,指的是一部分
● 切片 根据 步长step 从原序列中取出一部分元素组成新序列
● 切片适用于 字符串、列表、元组
切片的格式
字符串[开始索引:结束索引:步长]
"""

ss = "天青色的烟雨，而我在等你"
print(ss[0:3])  # 天青色
print(ss[:3])  # 天青色
print(ss[3:6])  # 的烟雨
print(ss[3:])  # 的烟雨，而我在等你
print(ss[:])  # 复制一份内容

print("--------------------------------------")
#倒叙
print(ss[3:-2])
# 步长
print(ss[:6:1])
print(ss[:6:2])
# 步长为负数
print(ss[5:1:-1])
print(ss[::-1])  # 所有内容倒叙