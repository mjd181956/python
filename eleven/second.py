#创建多重目录
import os

#获取当前工作目录
print("获取当前工作目录："+os.getcwd())

# #创建文件夹
# os.mkdir("新建的文件夹")
# print("文件夹创建成功")

# #创建子文件夹
# os.mkdir(r"新建的文件夹\子文件夹")
# print("子文件夹创建成功")

# #创建子文件夹的子文件夹
# os.mkdir(r"新建的文件夹\子文件夹\子子文件夹")
# print("子子文件夹创建成功")

#上面的方法虽然可以实现子文件夹的创建，但是比较麻烦，下面这个比较简单


#创建文件夹及子文件夹
os.makedirs(r"eleven\new\subfolder\Subfolders")
print("文件夹创建成功")


