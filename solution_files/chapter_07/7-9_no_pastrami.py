# 7-9_no_pastrami 20250613 SKNEO
# 三明治生产系统（含原料缺货处理）

待制作订单 = [
    '熏牛肉三明治', '蔬菜三明治', '烤奶酪三明治', '熏牛肉三明治',
    '火鸡三明治', '烤牛肉三明治', '熏牛肉三明治'
]

已完成订单 = []
缺货原料 = '熏牛肉'

print("=== 三明治厨房管理系统 ===")
print(f"\n⚠️ 很抱歉，今日{缺货原料}已售罄，相关订单将取消")

# 移除所有含缺货原料的订单
while 缺货原料 in 待制作订单:
    待制作订单.remove(缺货原料)

# 显示剩余订单
print(f"\n当前有效订单：{len(待制作订单)}份")
for 序号, 三明治 in enumerate(待制作订单, 1):
    print(f"{序号}. {三明治}")

# 生产流程
print("\n=== 开始生产 ===")
while 待制作订单:
    当前三明治 = 待制作订单.pop()
    print(f"\n👨‍🍳 正在制作：{当前三明治}")

    # 模拟制作过程
    import time

    time.sleep(1)  # 制作耗时

    已完成订单.append(当前三明治)
    print(f"✅ 已完成：{当前三明治}")

# 生产报告
print("\n=== 今日生产报告 ===")
print(f"\n总完成量：{len(已完成订单)}份")
for 三明治 in 已完成订单:
    print(f"- {三明治}")

print(f"\n已取消的{缺货原料}订单：3份")

sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
