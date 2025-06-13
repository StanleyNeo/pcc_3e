# 7-5_movie_tickets 20250613
# 方式1：while条件判断 输入
print("\n=== 电影票计费系统（条件判断版）===")
while True:
    age = input("请输入年龄（数字）或输入'退出'结束：")
    if age == '退出':
        break

    age = int(age)
    if age < 3:
        print("  👶 3岁以下免费")
    elif 3 <= age <= 12:
        print("  🧒 3-12岁票价：10美元")
    else:
        print("  🧑 12岁以上票价：15美元")

# 方式2：使用active变量
print("\n=== 电影票计费系统（变量控制版）===")
active = True
while active:
    age = input("请输入年龄（输入'quit'退出）：")
    if age.lower() == 'quit':
        active = False
    else:
        age = int(age)
        # 票价计算逻辑同上...

# 方式3：直接break退出
print("\n=== 电影票计费系统（break版）===")
while True:
    age = input("请输入年龄：")
    if age.lower() == 'quit':
        break
    # 票价计算逻辑...

# 中文优化版
print("\n=== 影院票务系统 ===")
print("票价标准：")
print("- 3岁以下：免费")
print("- 3-12岁：80元")
print("- 12岁以上：120元")

while True:
    年龄 = input("\n请输入观众年龄（输入'结束'退出）：")
    if 年龄 == '结束':
        print("感谢使用票务系统！")
        break

    try:
        年龄 = int(年龄)
        if 年龄 < 3:
            print("  👶 可免费入场")
        elif 3 <= 年龄 <= 12:
            print("  🧒 儿童票：80元")
        else:
            print("  🧑 成人票：120元")
    except:
        print("⚠️ 请输入有效年龄数字")

prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
