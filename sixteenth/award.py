import xlwings as xw
import random
import time

#创建工作簿
app = xw.App(visible=True,add_book=False)

#在实例中创建工作簿
workbook = app.books.add()

#在工作簿中创建工作簿
excelist = []
flag=12
for i in range(12):
    Excelbook=workbook.sheets.add(str(flag)+"月份")
    excelist.append(Excelbook)
    flag -= 1

#模拟数据
firstName = ["张","龙","赵","钱","孙","李","王","周","吴","邱","舒","佟","冯","陈","朱","戴","史","孔","腾","尹","路","宋","欧阳","杜","苏","卢","黄","段","乔","吕","魏"]
lastName = ["纯","超","雪","赛","家","丽","礼","林","琳","奇","聪","克","果","宏","凤","瑞金","娜","立","阳","文","羽","文宇","化吉","妹","波","博","钰","秀","峰","皇","潘","操","莉","云","化腾","招娣","成督","小川","玉淑","田","超","亮","梁","刚","靳东"]
xueLiName = ["本科","硕士","研究生","博士","博士后"]
addressName = ["北京市","天津市","上海市","重庆市","河北省","山西省","辽宁省","吉林省","黑龙江省","江苏省","浙江省","安徽省","福建省","江西省","山东省","河南省","湖北省","湖南省","广东省","海南省","四川省","贵州省","云南省","陕西省","甘肃省","青海省","台湾省","内蒙古自治区","广西壮族自治区","西藏自治区","宁夏回族自治区","新疆维吾尔自治区","香港特别行政区","澳门特别行政区"]

#添加随机信息
def adddate(Excel):
    Excel.range("A1:F1").value=["姓名","贡献级别","学历","奖励","地区"]
    for i in range(2,100):
        name=random.choice(firstName)+random.choice(lastName)
        level=random.randint(1,10)
        xueli=random.choice(xueLiName)
        xinzi=random.randint(9000,30000)
        address=random.choice(addressName)
        newlist_value=[name,level,xueli,xinzi,address]
        
        newRange="A"+str(i)+":"+"F"+str(i) 
        Excel.range(newRange).value=newlist_value

#删除sheet1工作表
for i in workbook.sheets:
    if i.name=="Sheet1":
        i.delete()

#遍历工作表/并删除指定工作表
for Excel in workbook.sheets:
    adddate( )
    time.sleep(2)

#对数据进行保存，并关闭工作簿
workbook.save("华为奖励表.xlsx")
workbook.close()
app.quit()



