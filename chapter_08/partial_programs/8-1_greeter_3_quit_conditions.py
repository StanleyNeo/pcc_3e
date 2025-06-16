def 格式化姓名(名, 姓, 中间名=''):
    """生成标准格式的完整姓名（支持中间名）"""
    if 中间名:
        全名 = f"{姓} {中间名} {名}"
    else:
        全名 = f"{姓} {名}"
    return 全名.title()


print("=== 姓名录入系统 ===")
print("说明：输入'退出'可随时结束程序\n")

while True:
    # 姓输入
    姓 = input("请输入姓氏（中文请先输入姓）：").strip()
    if 姓.lower() in ['退出', 'q']:
        print("\n感谢使用姓名系统！")
        break

    # 名输入
    名 = input("请输入名字：").strip()
    if 名.lower() in ['退出', 'q']:
        print("\n感谢使用姓名系统！")
        break

    # 中间名可选
    中间名 = input("请输入中间名（若无请直接回车）：").strip()
    if 中间名.lower() in ['退出', 'q']:
        print("\n感谢使用姓名系统！")
        break

    # 处理并显示
    if 中间名:
        完整姓名 = 格式化姓名(名, 姓, 中间名)
        print(f"\n您好，{完整姓名}（{姓}·{中间名}·{名}）！")
    else:
        完整姓名 = 格式化姓名(名, 姓)
        print(f"\n您好，{完整姓名}！")

    # 使用记录
    with open("names_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{完整姓名}\n")

    print("姓名已保存至系统档案\n")

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")