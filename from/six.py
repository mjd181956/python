a={}
print(a)
b={"name":"Lily","age":18}
print(b)

c=dict()
print(c)

d=dict(name="scy",age=18)
print(d)

f=dict([("name","Tom"),("age",19)])
print(f)

k=['name','age','job']
v=['Scy','18','Programmer']
g=dict(zip(k,v))
print(g)

h=dict.fromkeys(["name","age","job"])
print(h)

#增加字典
dict1={'a':'1','b':2}
print(dict1)
dict1['c']='3'
print(dict1)

#删除字典元素
#删除的是最后一对键和值
dict1.popitem()
print(dict1)

#修改字典元素
dict2={'a':'c',2:13,(1,2):'b'}
print(dict2)
dict2['a']=10
dict2['b']='hello'
dict2['c']='World'
print(dict2)