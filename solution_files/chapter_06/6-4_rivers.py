# 6-4_著名河流 20250611 SKNEO

著名河流 = {
    '尼罗河': '埃及',
    '密西西比河': '美国',
    '弗雷泽河': '加拿大',
    '卡斯科奎姆河': '阿拉斯加',
    '长江': '中国',
}
# for key 河流, value 国家 in Dictionary著名河流.item() in pairs
print("\n")
for 河流, 国家 in 著名河流.items():
    print(f"{河流}流经{国家}")

print("\n数据集中包含以下河流：")
for 河流 in 著名河流.keys():  # print keys()
    print(f"- {河流}")

print("\n数据集中包含以下国家/地区：")
for 国家 in 著名河流.values(): # print values()
    print(f"- {国家}")

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")
