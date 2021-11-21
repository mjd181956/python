#文件的删改查
import os
import time

#获取当前工作目录
print("获取当前工作目录为："+os.getcwd())

#创建文件 ——增
with open(r"eleven\new\new_book.txt","w") as file:
    file.write("这是一个新文本文件")
time.sleep(1)

#修改文件名字 -改
os.rename(r"eleven\new\new_book.txt",r"eleven\new\新文本.txt")
time.sleep(1)
print("修改成功")

#查询文件带下 -查
size=os.path.getsize(r"eleven\new\新文本.txt")
time.sleep(1)
print("文件大小为%s"%size)

#删除文件 -删
os.remove(r"eleven\new\新文本.txt")
time.sleep(1)
print("删除成功")