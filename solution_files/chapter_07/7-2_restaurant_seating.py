# 7-2_restaurant_seating 20250612 SKNEO
# 7-2_餐厅订位系统

人数 = input("\n请问您今晚有几位用餐？")
人数 = int(人数)

if 人数 > 12:  # 中国餐厅常见大桌标准 12
    print("当前预计等待时间：30分钟")
    print("您也可以选择分桌用餐")
else:
    print("\n✅ 您的餐桌已准备好！")

print("=== 餐厅订位系统 ===")

while True:
    try:
        人数 = input("\n请问您今晚有几位用餐？")
        人数 = int(人数)

        if 人数 <= 0:
            print("⚠️ 请输入有效的用餐人数")
            continue

        if 人数 > 12:  # 中国餐厅常见大桌标准
            print("\n抱歉，12人以上需提前1天预定")
            print("当前可提供2张6人桌拼桌")
        elif 人数 > 8:
            print("\n温馨提示：8人以上需等待大桌")
            print("当前预计等待时间：30分钟")
            print("您也可以选择分桌用餐")
        else:
            print("\n✅ 您的餐桌已准备好！")
            print(f"请跟随服务员前往{人数}人区")

        # 附加服务推荐
        if 人数 >= 6:
            print("\n我们可为6人以上团体提供：")
            print("- 专属套餐优惠")
            print("- 免费合影服务")

        break

    except ValueError:
        print("⚠️ 请输入数字，例如：3")

    # 退出选项
    选择 = input("\n是否重新输入人数？(y/n): ").lower()
    if 选择 != 'y':
        print("\n感谢您选择本餐厅！")
        break

party_size = input("How many people are in your dinner party tonight? ")
party_size = int(party_size)

if party_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")
