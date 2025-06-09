# 外星人无点数1第一个版本 20250609 SKNEO

alien_0 = {'color': 'green', 'speed': 'slow'}

alien_0['points'] = 5
point_value = alien_0.get('points', 'No point value assigned.')

print(point_value)