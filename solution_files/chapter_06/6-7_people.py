# Make an empty list to store people in.
# 6-7_显示所有人员信息 20250611 SKNEO

# 创建空列表存储人员信息
人员列表 = []

# 定义人员信息并添加到列表 keys and values
人员信息 = {
    '姓': '张',
    '名': '伟',
    '年龄': 35,
    '城市': '北京',
}
人员列表.append(人员信息)  # 人员信息 added in 空人员列表

人员信息 = {
    '姓': '李',
    '名': '小明',
    '年龄': 8,
    '城市': '上海',
}
人员列表.append(人员信息) # 人员信息 added in 人员列表

人员信息 = {
    '姓': '王',
    '名': '芳',
    '年龄': 28,
    '城市': '广州',
}
人员列表.append(人员信息) # 人员信息 added in 人员列表

# 显示所有人员信息
for 人员 in 人员列表:
    姓名 = f"{人员['姓']}{人员['名']}"
    年龄 = 人员['年龄']
    城市 = 人员['城市']

    print(f"{城市}的{姓名}今年{年龄}岁。")

people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 46,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'lemmy',
    'last_name': 'matthes',
    'age': 2,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 11,
    'city': 'sitka',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    
    print(f"{name}, of {city}, is {age} years old.")
