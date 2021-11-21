import os 
import time

#获取当前工作目录
print("获取当前工作目录："+os.getcwd())

#获取文件信息
def get_file():
    #获取当前工作目录的所有文件且保存到列表中
    files_save = []
    for root, dirs, files in os.walk(".\\"):
        for i in files:
            files_save.append(i)
    return files_save

#搜索文件信息
def get_find(name):
    global count
    count = 0
    for file in get_file():
        if name in file:
            print(file)
            count +=1

if __name__=="__main__":
    name=input("请输入您要搜索的文件名：")
    print("\n搜索成功----：")
    get_find(name)
    print("\n共为您搜索到{}条结果".format(count))
    