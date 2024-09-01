password = input("请输入密码")

container = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'

for ele in password:
    if ele not in container:
        print("密码不合法，包含非法字符", ele)
        break
else:
    print("密码合法")