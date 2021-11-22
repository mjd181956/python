f=open("./twelfth/myExcel.xls",'rb')
#创建文件句柄
date_excel=f.read()
#读取二进制
f.close()

f=open("./twelfth/myExcel-副本2.xls",'wb')
#二进制写入模式
f.write(date_excel)
f.close()