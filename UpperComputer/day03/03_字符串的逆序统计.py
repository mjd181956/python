"""
--------------------------------------------
您输入的字符串: zhongshanshan
长度: 13
逆序后为: nahsnahsgnohz
字符统计结果: z:1 h:3 o:1 n:3 g:1 s:2 a:2
--------------------------------------------
"""
temp = """
您输入的字符串:{}
长度: {}
逆序后为: {}
字符统计结果: {}
"""

while True:
    ss = input("请输入字符串：")
    if (len(ss) < 31):
        break
    else:
        print("字符串的长度必须小于31：！" + len(ss))

print(ss)

# 每一个字符对应出现的次数 zhangsansan
stat_dict = {}

# 遍历输入的每个字母
for s in ss:
    if s not in stat_dict:  # 字母不在字典中，将改字加入字典中
        stat_dict[s] = 1
        # print(stat_dict)
    else:
        # 字典中已经存在，就将增加它的值
        stat_dict[s] += 1

output_list = ["{}:{}".format(k, v) for k, v in stat_dict.items()]
# print(output_list)
# print("|".join(output_list))
print("--------------------------------------------------")

# 统计并输入
print(temp.format(
    ss,
    len(ss),
    ss[::-1],
    " ".join(output_list)
))
