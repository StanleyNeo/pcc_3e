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
