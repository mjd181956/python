import xlrd
import xlwt
from xlutils.copy import copy
fwrokbook=xlrd.open_workbook('./thirteenth/style.xlsx')
sheet=fwrokbook.sheets()[0]
new_workbook=copy(fwrokbook)
new_sheet=new_workbook.get_sheet(0)
style=xlwt.XFStyle()
font=xlwt.Font()
font.name="宋体"
font.bold=True
font.height=20*20
font.italic=True #是否为斜体
font.colour_index=12 
style.font=font
#设置Alignment属性
alignments=xlwt.Alignment()
alignments.vert=xlwt.Alignment.VERT_TOP #水平方向上对齐
alignments.horz=xlwt.Alignment.HORZ_RIGHT #垂直方向右对齐
style.alignment=alignments
#-----------------------副本1的内容--------------------------
#设置Pattern属性
pattern=xlwt.Pattern()
pattern.pattern=xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour=3
style.pattern=pattern
#--------------------------------------------------------------
new_sheet.write(1,1,"格式控制",style)
#设置行高，列宽，可以清晰地看出对齐方式
new_sheet.col(1).width=256*60
new_sheet.row(1).height_mismatch=True
new_sheet.row(1).height=20*60
new_workbook.save('./thirteenth/style-副本1.xls')
