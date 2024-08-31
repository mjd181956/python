"""
输入一个文件名，统计文件中
- 注释行数
- 空行数
- 代码行数
"""
file_name = input("请输入一个文件名：")
comment_count = 0
blank_count = 0
code_count = 0
with open(file_name, encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # 
        if line.startswith("#"):
            comment_count += 1
        elif not line:
            blank_count += 1
        else:
            code_count += 1
            
print(comment_count, blank_count, code_count)