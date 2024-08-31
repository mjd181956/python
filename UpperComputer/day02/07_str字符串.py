string = "hello"
print(string[1])

print("----------------------判断")
print("abCD".isalpha())  # 纯字母
print("123".isdigit())  # 是否数字
print("一二三12".isnumeric())  # 支持汉字数字
print("abc".startswith("ab"))  # 以ab么开头
print("abc".endswith("c"))  # 以c么结

print("----------------------查找")
print("abc".find("b"))  # 1
print("abc".find("x"))  # 找不到内容 -1
print("abc".rfind("c"))  # right 返回下的最后一次出现的索引
print("www.itheima.com".rfind("."))  # right 返回下的最后一次出现的索引
print("abcdef.bcom".replace("b", "B", 2))

print("----------------------切割")
names_list = "张三|李四光|王大拿|呜呜五".split("|")
print(names_list, type(names_list))  # ['张三', '李四光', '王大拿', '呜呜五']
ss = "0123456789"
print(ss[4:7])

print("----------------------去空白")
print("  abc  ".strip())  # 去空白
