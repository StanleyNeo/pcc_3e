# 7-1_rental_car 20250612 SKNEO
# 7-1_汽车租赁服务
# 品牌白名单（可根据实际库存调整）
汽车品牌 = ['奥迪', '宝马', '奔驰', '特斯拉', '丰田', '本田']
print(汽车品牌 )
汽车 = input("请输入您想租赁的汽车品牌? ")

print("=== 汽车租赁服务 ===")

# 品牌白名单（可根据实际库存调整）
可用品牌 = ['奥迪', '宝马', '奔驰', '特斯拉', '丰田', '本田']

while True:
    try:
        品牌 = input("\n请输入您想租赁的汽车品牌：").strip()

        if not 品牌:  # 检查空输入
            raise ValueError("请输入有效品牌名称")

        if 品牌 not in 可用品牌:
            print(f"\n⚠️ 暂未提供{品牌}品牌，我们有以下品牌可选：")
            print(", ".join(可用品牌))
            continue

        print(f"\n正在为您查询{品牌}...")
        # 模拟查询过程
        import time

        time.sleep(1.5)

        print(f"\n✅ 找到可用车辆！可为您安排一辆{品牌}")
        break

    except ValueError as e:
        print(f"\n错误：{str(e)}")

    # 是否继续查询
    选择 = input("\n是否继续查询？(y/n): ").lower()
    if 选择 != 'y':
        print("\n感谢使用我们的租车服务！")
        break



print(f"正在为您查询 {汽车.title()}")

car = input("What kind of car would you like? ")

print(f"Let me see if I can find you a {car.title()}.")
