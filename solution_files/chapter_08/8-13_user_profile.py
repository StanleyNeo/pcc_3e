# 8-13_user_profile 函数 用户资料 20250617 Stanley Neo

def 创建用户资料(名, 姓, **其他信息):
    """
    构建包含用户完整资料的字典

    参数:
        名 (str): 用户名
        姓 (str): 用户姓
        **其他信息: 任意数量的关键字参数(用户额外信息)

    返回:
        dict: 包含用户完整资料的字典
    """
    用户资料 = {
        '姓名': f"{姓}{名}",  # 中文姓名顺序
        **其他信息  # 解包其他信息
    }
    return 用户资料


# 创建用户资料示例
用户资料1 = 创建用户资料('志明', '张',
                         居住地='北京',
                         职业='数据分析师',
                         技能=['Python', 'SQL', '机器学习'])

用户资料2 = 创建用户资料('美丽', '李',
                         公司='腾讯科技',
                         部门='人工智能研发',
                         职级='高级工程师',
                         兴趣=['爬山', '摄影'])

# 打印结果
print("【用户资料1】")
for 键, 值 in 用户资料1.items():
    print(f"{键}: {值}")

print("\n【用户资料2】")
for 键, 值 in 用户资料2.items():
    print(f"{键}: {值}")

# 扩展功能：从输入创建资料
if input("\n是否创建新用户资料？(y/n) ").lower() == 'y':
    名 = input("请输入名字: ")
    姓 = input("请输入姓氏: ")
    其他信息 = {}
    while True:
        键 = input("输入信息类型(如'职业')或直接回车结束: ")
        if not 键:
            break
        值 = input(f"请输入{键}: ")
        其他信息[键] = 值

    新资料 = 创建用户资料(名, 姓, **其他信息)
    print("\n新建用户资料:", 新资料)

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Stanley', 'Neo',
                             location='Jurong East',
                             field='Data Science')
print(user_profile)