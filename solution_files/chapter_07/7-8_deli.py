# 7-8_deli 20250613 SKNEO

# 三明治生产系统
待制作订单 = ['蔬菜三明治', '烤奶酪三明治', '火鸡三明治', '烤牛肉三明治']
已完成订单 = []
当前状态 = {
    '蔬菜三明治': '准备中',
    '烤奶酪三明治': '准备中',
    '火鸡三明治': '准备中',
    '烤牛肉三明治': '准备中'
}

print("=== 三明治厨房生产系统 ===")
print(f"\n当前待制作订单：{', '.join(待制作订单)}")

while 待制作订单:
    当前三明治 = 待制作订单.pop()

    # 更新生产状态
    当前状态[当前三明治] = '制作中'
    print(f"\n👨‍🍳 正在制作您的【{当前三明治}】")

    # 模拟制作过程
    import time

    time.sleep(1.5)  # 模拟制作耗时

    已完成订单.append(当前三明治)
    当前状态[当前三明治] = '已完成'
    print(f"✅ 已完成 {当前三明治}")

# 生产报告
print("\n=== 生产完成报告 ===")
print(f"\n总完成数量：{len(已完成订单)}份")
for 序号, 三明治 in enumerate(已完成订单, 1):
    print(f"{序号}. {三明治}")

# 状态查询功能
print("\n当前所有订单状态：")
for 产品, 状态 in 当前状态.items():
    print(f"- {产品}: {状态}")

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
