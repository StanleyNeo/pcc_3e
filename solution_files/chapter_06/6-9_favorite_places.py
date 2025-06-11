# 6-9_喜欢的地方 20250611 SKNEO

喜欢的地方 = {
    '张伟': ['黄山', '张家界', '九寨沟'],
    '李娜': ['三亚', '桂林'],
    '王强': ['泰山', '颐和园', '西湖']
}

for 姓名, 地点列表 in 喜欢的地方.items():
    print(f"\n{姓名}喜欢以下地方：")
    for 地点 in 地点列表:
        print(f"- {地点}")

favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt. verstovia', 'the playground', 'new hampshire']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")
