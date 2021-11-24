import xlrd
import xlwt
import os
from xlutils.copy import copy

fworkbook=xlrd.open_workbook('./thirteenth/Excel练习.xlsx')
sheet=fworkbook.sheets()[0]
new_workbook=copy(fworkbook)
new_sheet=new_workbook.get_sheet(0)
style=xlwt.XFStyle()
font=xlwt.Font()
font.name="宋体"
font.blod=True
font.height=20*20
font.italic=True
font.colour_index=12
style.font=font
#设置border属性
borders=xlwt.Borders()
borders.bottom=2
borders.left=3
borders.right=4
style.borders=borders
new_sheet.write(1,1,"格式控制",style)
new_workbook.save('./thirteenth/borderExcel.xls')
os.system(r".\thirteenth\borderExcel.xls")


