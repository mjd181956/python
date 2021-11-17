"第十章 文件的读取"
#open("文件路径"，“操作模式”)
#UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 65: illegal multibyte sequence在运行是出现了这样的错误，是
#因为编码格式不一样，所以可以用以下的格式进行编码的转换
file=open(r"f:\python\README.md","r",encoding="utf-8")
data=file.read()
file.close()
print(data)


#读取大量文件是可以使用readline
file1=open(r"f:\python\1.txt","r",encoding="utf-8")
date=file1.readline()
date1=file1.readlines()
file1.close()
print(date)
#print(date1)


#二进制文件读取
file2=open(r"D:\win\图片\23.PNG","rb")
data2=file2.readline()
file2.close()
print(data2)


#文本写入
file3=open(r"E:\VS2019\test.txt","w")
file3.write("我今天学习了文件的读写操作")
file3.close()


#文件的追加
file4=open(r"E:\VS2019\test.txt","a")
file4.write("\r再次追加测试文件按")
file4.close()

#当读取文件异常时的处理方法可以使用with
with open(r"E:\VS2019\test.txt","r")as file5:
    data3=file5.read()
    print(data3)
    "with open(“文件路径”，“操作模式”）as 变量名（文件对象）:"
        #不管是否出现异常都会关闭文件


#获取小说内容
def novel_data():
    with open(r"玄幻小说.txt","r",encoding="utf-8") as file6:
        novel=file6.read()
    print(novel)
    return novel
#对小说每个文字进行分割存储
def info_analyse():
    #遍历的值存储
    ucount=[]
    #统计次数
    data_count={}
    for i in novel_data():
        ucount.append(i)
        #若文字存在于ucount列表中，则次数+1
        if i in ucount:
            data_count[i]=data_count.get(i,0)+1
            #若文字存在于ucount列表中，给予初始值为0
        else:
            data_count[i]=data_count.get(i,0)
    data=list(data_count.items())
    return data
#对每个文字在小说出现次数进行分析排序
def info_ordinal():
    info_list=info_analyse()
    new_info_list=sorted(info_list,key=lambda x:x[1],reverse=True)
    print(new_info_list)
#住程序入口
if __name__=="__main__":
    info_ordinal() 


#生成一个csv表格
def create_csv():
    with open("studnet_info.csv","w") as file7:
        file7.write("姓名,学号,班级,性别\n")
        file7.write("张三,1,1 班,男\n")
        file7.write("李四,2,1 班,男\n")
        file7.write("小美,3,1 班,女\n")
        file7.write("小芳,4,1 班,女\n")
if __name__=="__main__":
    create_csv()
    print("csv文件已生成")    


#电话备忘录
'存储号码'
def write_info(name,tep):
    with open("data.txt","a") as file8:
        file8.write("{},{}\n".format(name,tep))
'读取号码'
def read_info():
    with open("data.txt","r") as file9:
        data=file9.read()
        print(data)
def main():
    print("1-存储号码 2-查询号码")
    while 1:
        command=eval(input("请输入您要进行的操作："))
        if command==1:
            name=input("请输入朋友名字：")
            tep=input("请输入朋友电话：")
            write_info(name,tep)
            print("电话号码存储成功\n")
        elif command==2:
            print("\n查询成功")
            read_info()
        else:
            print("请输入正确操作")
if __name__=="__main__":
    main()

