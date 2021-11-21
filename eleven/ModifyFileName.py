import os
import time

#获取所有文件名
file_name=[]
for root,dirs,files in os.walk(r".\eleven\new"):
    for i in files:
        file_name.append(i)

#修改所有文件名
count=0
for i in file_name:
    count+=1
    #文件原名
    old_path=r".\eleven\new\\"+i
    #新文件名
    new_path=r".\eleven\new\\"+str(count)+".txt"
    os.rename(old_path,new_path)
print("修改成功")