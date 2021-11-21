import os
import time

#获取当前工作目录
print("获取当前工作目录为："+os.getcwd())

#创建一个文件夹
os.mkdir("创建文件夹")
print("创建成功")
time.sleep(1)

#修改文件夹名称
os.rename("创建文件夹","修改文件夹名")
print("文件夹名修改成功")
time.sleep(1)

#删除文件夹
os.rmdir("修改文件夹名")
print("文件夹删除成功")
time.sleep(1)