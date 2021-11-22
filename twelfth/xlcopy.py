'Excel工作表数据复制'
import xlrd
import xlwt
#导入xlutil的copys属性
from xlutils.copy import copy
#首先进行读取
workbook=xlrd.open_workbook('./twelfth/myExcel.xls')#,formatting_info=True
sheet=workbook.sheets()[0]

#进行复制
new_workbook=copy(workbook)
new_sheet=new_workbook.get_sheet(0)
# 保存
new_workbook.save('./twelfth/myExcel-副本.xls')
