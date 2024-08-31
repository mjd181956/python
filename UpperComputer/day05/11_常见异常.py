def index_error(index):
    try:
        lst = [3, 2, 5]
        print(lst[index])
    except IndexError:
        print("Index out of range")
 
def key_error(key):
    age = {"张三": 33, "李四": 44}
    try:
        print(age[key])
        print(d[key])
    except KeyError as e:
        print(f"{key} 不存咋")       
        
if __name__ == '__main__':
    index_error(3)
