# 6-8_宠物 20250611 SKNEO
# 创建空列表存储宠物信息
宠物列表 = []

# 定义宠物信息并添加到列表
宠物 = {
    '动物类型': '蟒蛇',
    '名字': '小花',
    '主人': '张伟',
    '体重(kg)': 43,
    '食物': '昆虫',
}
宠物列表.append(宠物)

宠物 = {
    '动物类型': '鸡',
    '名字': '小白',
    '主人': '李娜',
    '体重(kg)': 2,
    '食物': '谷物',
}
宠物列表.append(宠物)

宠物 = {
    '动物类型': '狗',
    '名字': '小黑',
    '主人': '王强',
    '体重(kg)': 37,
    '食物': '狗粮',
}
宠物列表.append(宠物)

# 显示每只宠物的信息
for 宠物 in 宠物列表:
    print(f"\n关于{宠物['名字']}的信息：")
    for 属性, 值 in 宠物.items():
        print(f"\t{属性}：{值}")

# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
