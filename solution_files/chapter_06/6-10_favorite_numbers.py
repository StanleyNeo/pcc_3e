# 6-10_喜欢的数字 20250611 SKNEO

喜欢的数字 = {
    '小美': [6, 8],          # 6和8在中国文化中代表顺利和发财
    '小明': [8, 9, 3],       # 9代表长久，3在部分地区有特殊含义
    '小刚': [5, 2],          # 5在中国文化中代表"我"，2代表"爱"
}

for 姓名, 数字列表 in 喜欢的数字.items():
    print(f"\n{姓名}喜欢的数字有：")
    for 数字 in 数字列表:
        print(f"  {数字}")

favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}")
