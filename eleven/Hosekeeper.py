"简易文件管家"
import os

#选择工作目录
def choice_path():
    path=input("请选择您要进入的工作目录：")
    os.chdir(path)
    case_path=os.getcwd()
    print("已进入工作目录："+case_path)

#获取文件或者文件夹名
def execute():
    global save_file
    print("\n 获取成功 =====")
    #存储信息
    save_file=[]
    #获取所有的文件名
    for root, dirs, files in os.walk(".\\"):
        for i in files:
            print(i)
            save_file.append(i)
        break
    return save_file

#展示文件信息
def showinfo():
    print("\n")
    for i in execute():
        print(i)

#修改文件
def modify_info():
    print("""
            ==========您要进行的操作是==============
              1 - 序号修改文件名     2 - 删除文件
    """)
    command2=input("请输入您的文件操作：")

    #序号方式命名文件
    if command2 == "1":
        count=0
        for i in save_file:
            count+=1
            path=".\\"
            old=path+i
            types=i.split(".")
            new=path+str(count)+"."+types[1]
            os.rename(old,new)
            print("文件修改成功")
    
    #删除文件
    elif command2== "2":
        for i in save_file:
            path=".\\"
            old=path+i
            os.remove(old)
            print("文件删除成功")

#主程序入口
if __name__=="__main__":
    choice_path()
    showinfo()
    modify_info()