# import xlrd

# Excelbook=xlrd.open_workbook(r"F:\python\twelfth\text.xlsx")

# #通过open_workbook函数，加载文件夹中的xlsx工作簿文件
# print(Excelbook)

# sh1=Excelbook.sheet_by_index(0)
# cellvalue1=sh1.cell_value(rowx=0,colx=0)
# cellvalue2=sh1.cell(4,1).value
# print(cellvalue1)
# print(cellvalue2)
# sh2=Excelbook.sheet_by_name("Sheet1")
# sh3=Excelbook.sheets()[0]



import xlwt
new_workbook=xlwt.Workbook()
sheet=new_workbook.add_sheet('text_sheet')

sheet.write(0,0,'姓名')
sheet.write(0,1,'年龄')
sheet.write(0,2,'班级')
sheet.write(0,3,'考场号')

name_list=['姓名','年龄','班级','考场号']
for i in name_list:
    sheet.write(1,name_list.index(i),i)

data=[
    {
        'name':'小张',
        'age':'12',
        'gender':'男',
        'grand':'5年级'
    },
    {
        'name':'小王',
        'age':'10',
        'gender':'男',
        'grand':'3年级'
    },
    {
        'name':'小赵',
        'age':'8',
        'gender':'女',
        'grand':'2年级'
    },
]

for i,item in enumerate(data):
    print(i)
    print(item)
    sheet.write(i+2,0,item['name'])
    sheet.write(i+2,1,item['age'])
    sheet.write(i+2,2,item['gender'])
    sheet.write(i+2,3,item['grand'])
#保存文件
new_workbook.save('./twelfth/myExcel.xls')
