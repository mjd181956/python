import xlrd
import xlwt

workbook=xlwt.Workbook()
worksheet=workbook.add_sheet("零食售卖清单")
#设置样式1：
def style0():
    style=xlwt.XFStyle()
    font=xlwt.Font()
    font.name="黑体"
    font.bold=True
    font.height=20*20
    style.font=font
    borders=xlwt.Borders()
    borders.top=1
    borders.bottom=1
    borders.left=1
    borders.right=1
    style.borders=borders
    pattern=xlwt.Pattern()
    pattern.pattern=xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour=44
    style.pattern=pattern
    alignments=xlwt.Alignment()
    alignments.horz=xlwt.Alignment.HORZ_CENTER
    style.alignment=alignments
    return style

#设置样式1
def style1():
    style=xlwt.XFStyle()
    font=xlwt.Font()
    font.name="宋体"
    font.height=20*18
    font.bold=False
    style.font=font
    border=xlwt.Borders()
    border.top=1
    border.bottom=1
    border.left=1
    border.right=1
    style.borders=border
    pattern=xlwt.Pattern()
    pattern.pattern=xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour=22 
    style.pattern=pattern
    alignments=xlwt.Alignment()
    alignments.horz=xlwt.Alignment.HORZ_CENTER
    style.alignment=alignments
    return style

#设置样式2：
def style2():
    style=xlwt.XFStyle()
    font=xlwt.Font()
    font.name="宋体"
    font.height=20*18
    style.font=font
    border=xlwt.Borders()
    border.top=1
    border.bottom=1
    border.left=1
    border.right=1
    style.borders=border
    alignments=xlwt.Alignment()
    alignments.horz=xlwt.Alignment.HORZ_CENTER
    style.alignment=alignments
    return style

style0=style0()
style1=style1()
style2=style2()

goods={
    "商品 id":["品名","数量","单位","单价","总"],
    21323:["面包",5,"包",23],
    46456:["鸡蛋卷",4,"包",42],
    45645:["鸡翅",1,"千克",33],
    754557:["牛肉干",2,"千克",45],
    456456:["火腿肠",4,"箱",67],
    456546:["巧克力",2,"箱",49],
    73454:["山楂",4,"箱",14],
    234:["鸡肉",23,"千克",56]
}
i=0
for key,value in goods.items():
    worksheet.col(i).width=256*20
    if i==0:
        worksheet.write(i,0,key,style0)
    elif i>0 and i%2 == 1:
        worksheet.write(i,0,key,style1)
    else:
        worksheet.write(i,0,key,style2)

    for j in range(len(value)):
        if i==0:
            #写入i行，列表下标+1列，写入数据：列表下标对应的元素
            worksheet.write(i,j+1,value[j],style0)
        elif i>0 and i%2 == 1:
            worksheet.write(i,j+1,value[j],style1)
        else:
            worksheet.write(i,j+1,value[j],style2)
    i+=1
#追加数据
m=0
for key,value in goods.items():
    if m>0:
        if m%2==1:
            worksheet.write(m,len(value)+1,value[1]*value[3],style1)
        else:
            worksheet.write(m,len(value)+1,value[1]*value[3],style2)
    m += 1
#保存
workbook.save('./fourteenth/零食售卖清单-副本.xls')