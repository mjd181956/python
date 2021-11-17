name="Rossum"
num=len(name)
print(num)

list=["小明","Guido",666,True]
print(list)
list.append("张三")
print(list)

list.extend(["王五","qiaozhi"])
print(list)

list.insert(2,"小杜")
print(list)

student=["小明","小张","小武"]
index=student.index("小张")
print(index)

check = "小武" in student
print(check)

for i in student:
    if "小张" == i:
        print("存在")
        break

student[1]="小王"
print(student)

#student.clear()
#print(student)

#student.pop(2)
#print(student)

student.remove("小明")
print(student)

list1=[3,2,8,6,12]
list2=["and","long","Jack","HeroLong"]
list1.sort()
list2.sort()
print(list1)
print(list2) 

list1.sort(reverse=True)
print(list1)
