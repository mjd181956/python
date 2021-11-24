#导入读写模块
import xlrd
import xlwt
from xlutils.copy import copy

#首先进行读取
workbook=xlrd.open_workbook('./thirteenth/Excel练习.xlsx')
sheet=workbook.sheets()[0]

#进行复制
new_workbook=copy(workbook)
new_sheet=new_workbook.get_sheet(0)
#设置列宽，256为一个衡量单位
new_sheet.col(1).width=256*40
#设置行高，20是1个衡量单位
new_sheet.row(1).height_mismatch=True
new_sheet.row(1).height=20*60

new_workbook.save('./thirteenth/myExcel练习.xls')
