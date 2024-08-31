"""
需求
输入文件的名字，然后程序自动完成对文件进行备份
分析

1.输入文件名 b.py
2.创建文件  文件名[复制].py
3.读取文件, 写入到复制的文件中
"""
import os

file_name = None
while True:
    file_name = input("请输入文件名: ")

    # 首先判断文件存在，不存在使其重新输入
    if os.path.exists(file_name):
        break
    
    print(f"文件【{file_name}】不存在")
    
print(file_name)
# 生成新的文件名
dot_index = file_name.rfind(".")
file_name_prefix = file_name[:dot_index]    # 文件名
file_name_suffix = file_name[dot_index:]    # 后缀名

new_file_name = file_name_prefix + "[复制]" + file_name_suffix
print("copy to: ", new_file_name)

with open(new_file_name, "rb") as new_f:
# 读取原来文件
    bytes_data = new_f.read()
    print(type(bytes_data), len(bytes_data))
# 创建新文件, 写入新文件
    with open(new_file_name, "wb") as new_file:
        new_file.write(bytes_data)

