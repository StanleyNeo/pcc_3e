# 8-12_sandwiches 函数 制作三明治 20250617 Stanley Neo

def 制作三明治(*配料):
    """
    根据提供的配料制作三明治

    参数:
        *配料: 可变数量的配料参数
    """
    print("\n🥪 正在为您制作三明治：")

    # 检查是否提供了配料
    if not 配料:
        print("⚠️ 您没有提供任何配料，制作了空气三明治！")
        return

    # 显示添加的配料
    for 序号, 食材 in enumerate(配料, 1):
        print(f"  {序号}. 正在添加：{食材}")

    # 根据配料数量给出不同评价
    if len(配料) >= 4:
        print("✨ 豪华三明治制作完成！请享用！")
    elif len(配料) >= 2:
        print("✅ 标准三明治制作完成！")
    else:
        print("🍞 基础三明治制作完成，建议添加更多配料哦！")


# 制作不同种类的三明治
制作三明治('烤牛肉', '切达奶酪', '生菜', '蜂蜜芥末酱')
制作三明治('火鸡肉', '苹果片', '蜂蜜芥末')
制作三明治('花生酱', '草莓酱')
制作三明治()  # 测试无配料情况

# 扩展功能：询问用户想要的配料
if input("\n是否要定制三明治？(y/n) ").lower() == 'y':
    用户配料 = input("请输入想要的配料，用逗号分隔：").split(',')
    制作三明治(*[配料.strip() for 配料 in 用户配料])

def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')
