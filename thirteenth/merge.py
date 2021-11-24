import xlrd
import xlwt
from xlutils.copy import copy
fworkbook=xlrd.open_workbook('./thirteenth/style.xlsx')
sheet=fworkbook.sheets()[0]
new_workbook=copy(fworkbook)
new_sheet=new_workbook.get_sheet(0)
style=xlwt.XFStyle()
font=xlwt.Font()
font.name="宋体"
font.bold=True
font.height=20*20
font.italic=True
font.colour_index=12
style.font=font
alignments=xlwt.Alignment()
alignments.vert=xlwt.Alignment.VERT_TOP
alignments.horiz=xlwt.Alignment.HORZ_RIGHT
style.alignment=alignments

pattern=xlwt.Pattern()
pattern.pattern=xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour=3
style.pattern=pattern
#合并单元格
new_sheet.write_merge(2,4,3,5,"格式样式",style)
new_workbook.save('./thirteenth/merge.xls')