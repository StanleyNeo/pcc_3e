# 5-10 20250608 检查用户名

current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")

# 当前已注册的用户名列表（使用中文）
当前用户表 = ["小明", "小红", "大强", "李雷", "韩梅梅"]

# 新用户想注册的用户名列表（包含重复）
新用户表 = ["小红", "韩梅梅", "张伟", "王芳", "赵强"]

# 将当前用户名转换为小写（为了兼容含大小写的情况，尽管中文不受影响）
当前用户小写 = [用户.lower() for 用户 in 当前用户表]

# 检查新用户名是否已存在
for 新用户 in 新用户表:
    if 新用户.lower() in 当前用户小写:
        print(f"对不起，用户名『{新用户}』已被使用，请换一个用户名。")
    else:
        print(f"用户名『{新用户}』可以使用。")

# 对不起，用户名『小红』已被使用，请换一个用户名。
# 对不起，用户名『韩梅梅』已被使用，请换一个用户名。
# 用户名『张伟』可以使用。
# 用户名『王芳』可以使用。
# 用户名『赵强』可以使用。
