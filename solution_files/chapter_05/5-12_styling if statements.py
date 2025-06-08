# 5-12 styling if statements

# 在 Python 中，良好的 if 语句风格包括：
#
# 适当使用缩进（4 个空格）
#
# 简洁明确的逻辑表达式
#
# 布尔值不要与 True 或 False 比较
#
# 合理使用 elif 和 else
#
# 避免不必要的比较或冗余代码

# 示例 1：检查用户名是否存在（来自 5-10 改进）
current_users = ["alice", "bob", "charlie"]
new_users = ["bob", "dave", "Alice"]

# 转换为小写以进行不区分大小写比较
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"对不起，用户名『{new_user}』已被使用。")
    else:
        print(f"用户名『{new_user}』可以使用。")

# 示例 2：判断人的年龄阶段
age = 25

if age < 2:
    print("你是一个婴儿。")
elif age < 4:
    print("你是一个蹒跚学步的小孩。")
elif age < 13:
    print("你是一个儿童。")
elif age < 20:
    print("你是一个青少年。")
elif age < 65:
    print("你是一个成年人。")
else:
    print("你是一个老年人。")

# 示例 3：检查是否为空列表
users = []

if users:
    for user in users:
        print(f"欢迎，{user}！")
else:
    print("用户列表为空，请添加用户。")

# ✅ 小结：良好的 if 语句风格建议
# 建议内容	示例
# 使用 4 个空格缩进	✅ if 条件:\n 执行代码
# 不用与 True/False 直接比较	✅ if is_active:
# 使用 elif 而不是多个 if	✅ if ... elif ... else
# 简洁地检查空列表/字符串/字典等	✅ if not list:
# 使用明确的比较操作符	✅ if age < 18: