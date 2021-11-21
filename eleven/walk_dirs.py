import os 
import time

#获取当前工作目录
print("当前工作目录为："+os.getcwd())
#获取walk方法返回的数据
print(os.walk("\\"))
def get_file():
    for root,dirs,files in os.walk(".\\"):
        #print(dirs)
        print(files)
get_file()
