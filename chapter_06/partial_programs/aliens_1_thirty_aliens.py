# 外星人_1三十个外星人 20250609 SKNEO
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens)
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

外星人列表 = []
# 创建30个绿色外星人
for 外星人编号 in range(30):
    新外星人 = {'颜色': '绿色', '分数': 5, '速度': '慢'}
    外星人列表.append(新外星人)
print(外星人列表)

# 显示前5个外星人
for 外星人 in 外星人列表[:5]:
    print(外星人)
print("...")