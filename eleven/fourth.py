"文件的查询"
import os
import time

#获取当前工作目录
print("获取当前工作目录:"+os.getcwd())

#获取walk方法返回的数据
print(os.walk(".\\"))

#获取当前目录下的所有文件和文件夹
alls=os.listdir(".\\from")

#创建txt文件名保存列表
save_date=[]
#对所有文件和文件夹进行判断，是否为txt文件
for i in alls:
    if ".txt" in i:
        #若为txt文件则添加到列表
        save_date.append(i)
    else:
        pass
print(save_date)

def get_file():
    for root,dirs,files in os.walk(".\\"):
        print(root,dirs,files)

get_file()

def main():
    pass


if __name__ == "__main__":
    main()

