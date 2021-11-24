import xlrd
import xlwt

from xlutils.copy import copy

fworkbook=xlrd.open_workbook('./thirteenth/Excel练习.xlsx')
sheet=fworkbook.sheets()[0]
new_workbook=copy(fworkbook)
new_sheet=new_workbook.get_sheet(0)
#初始化样式(创建样式对象)
style=xlwt.XFStyle()

#创建属性对象，这里使用字体属性做例子说明
font=xlwt.Font()
#对属性的值进行初始化
font.name="宋体"
font.bold=False #是否加粗
font.height=20*20   #字号*20
#将赋值好的属性对象赋值给style的对应的属性
style.font=font
new_sheet.write(1,1,"格式控制",style)
new_workbook.save('./thirteenth/Excelbold.xls')

