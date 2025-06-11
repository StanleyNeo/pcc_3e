# 将前3个绿色外星人改为黄色 20250611 SKNEO

# 创建一个空列表用于存储外星人
外星人列表 = []

# 创建30个绿色外星人
for 编号 in range(30):
    新外星人 = {'颜色': '绿色', '分数': 5, '速度': '慢'}
    外星人列表.append(新外星人)

# 将前3个绿色外星人改为黄色
for 外星人 in 外星人列表[:3]:
    if 外星人['颜色'] == '绿色':
        外星人['颜色'] = '黄色'
        外星人['速度'] = '中速'
        外星人['分数'] = 10

# 显示前5个外星人
for 外星人 in 外星人列表[:5]:
    print(外星人)
print("...")

# 显示已创建的外星人总数
print(f"外星人总数: {len(外星人列表)}")

aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")