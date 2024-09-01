def create_user(username, password, is_admin = False, is_active = True, is_verified = False):
    print("创建用户...")
    print(f"用户名: {username}")
    print(f"密码: {password}")
    print(f"是否管理员: {is_admin}")
    print(f"是否激活: {is_active}")
    print(f"是否验证: {is_verified}")
    print("用户创建成功!------------------------")
    
if __name__ == '__main__':
    create_user("join","password")
    create_user("join", "password", is_admin=True)
    create_user("join", "password", is_active=False, is_verified=True)
