"""
需求：
1. 定义布尔型变量 has_ticket 表示是否有车票
2. 定义整型变量 knife_length 表示刀的长度，单位：厘米
3. 首先检查是否有车票，如果有，才允许进行 安检
4. 安检时，需要检查刀的长度，
5. 判断是否超过 20 厘米
  a. 如果超过 20 厘米，提示刀的长度，不允许上车
  b. 如果不超过 20 厘米，安检通过
6. 如果没有车票，不允许进门
"""

has_ticket = eval(input("请输入是否有车票（True/False）："))  # 1 0
knife_length = int(input("请输入刀的长度（单位：厘米）："))

if has_ticket:
    print("邮票", has_ticket)
    if knife_length <= 20:
        print("安检通过，可以上车", knife_length)
    else:
        print("不能上车，刀太长", knife_length)
else:
    print("没有车票，不准进门")
