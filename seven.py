#内建函数
#name= input("请输入您的名字：")
#内建函数
#print("您的名字叫："+name)

def play():
    print("小明爱玩")

#自定义函数调用
play()


# def get_name():
#     name=input("请输入您的名字：")
#     return name

# my_name=get_name()
# print("函数获取到的返回值为："+my_name)

# def execute():
#     name="小明"
#     age=18
#     return age
    
# print(type(execute()))


# def execute():
#     name="小明"
#     age=18
#     list_data=[name,age]#列表类型
#     dic_data={age:name} #字典类型
#     tup_data=(name,age) #元组类型
#     set_data={name,age} #集合类型
#     return list_data

# print(type(execute()))


# def attrs(name,age):
#     get_name=name   #函数体（把指定形式参数赋值给变量）
#     get_age=age
#     print(name,age)

# attrs("小明","9岁") #调用函数，同时传递实际参数给函数


'任意位置传递参数'
# def attrs(name,age):
#     get_name=name
#     get_age=age
#     print(name,age)

# attrs(age="9岁",name="小明")

"函数特性之默认参数"
# def attrs(name,age,sex="男"):
#     get_name=name
#     get_age=age
#     get_sex=sex
#     print(name,age,sex)

# attrs(age="9岁",name="小明")

"可变参数"
# def add(*arg):
#     count=0
#     for i in arg:
#         count=count+i
#     print("arg的数据类型为：",type(arg))    #在函数内部会自动识别为元组
#     print(arg)
#     return count

# result=add(1,2,3,4,5)
# print("函数返回的之为：",result)


# def add(*arg):
#     count=0
#     for i in arg:
#         count=count+i
#     print(type(arg))    #arg在函数内部会制动识别为元组或者列表
#     print(arg)
#     return count

# num=[1,2,3,4,5,6]
# result=add(*num)
# print(result)

# def add(arg):
#     count=0
#     for i in arg:
#         count=count+i
#     print(type(arg))    #arg在函数内部会制动识别为元组或者列表
#     print(arg)
#     return count

# num=[1,2,3,4,5,6]
# result=add(num)
# print(result)

"可变参数**kw"
# def get_name(**kw):
#     print(type(kw)) #dict 字典类型
#     print(kw)
#     print(kw["name"])

# get_name(name="小明",age="19")

'关键字global,将函数内部的变量变成全局变量'
def variable():
    global var_data
    #局部变量var_data
    var_data="123"
    data="1235"

#全局变量data
data="123"
#调用函数
variable()
print(var_data, data)





