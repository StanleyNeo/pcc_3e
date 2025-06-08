usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for loggin in again!")
else:
    print("We need to find some users!")

用户名 = []

if 用户名:

    for 用户 in 用户名:
        if 用户 == '管理员':
            print("您好，管理员，您想查看状态报告吗？")
        else:
            print(f"您好，{用户}，感谢您再次登录！")
else:
    print("我们需要找到一些用户！")
