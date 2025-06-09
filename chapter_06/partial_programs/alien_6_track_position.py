# 外星人6号移动距离位置 20250609 SKNEO
外星人_0 = {'X位置': 0, 'Y位置': 25, '速度': '中等'}
print(f"原始位置：{外星人_0['X位置']}")

# 将外星人向右移动。
# 根据外星人当前速度确定移动距离。
if 外星人_0['速度'] == '慢速':
    X增量 = 1
elif 外星人_0['速度'] == '中等':
    X增量 = 2
else :
    # 这肯定是一个快速外星人。
    X增量 = 3

# 新位置等于旧位置加上增量。
外星人_0['X位置'] = 外星人_0['X位置'] + X增量

print(f"新位置：{外星人_0['X位置']}")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")