# 20250606 SKNEO
# 自行车

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

bikes = ['trek', 'cannondale', 'redline', 'specialized']
message = f"我的第一辆自行车是 {bicycles[0].title()}。"

print(message)

# 汽车 = ['宝马', '奥迪', '丰田', '斯巴鲁']

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

cars = ['宝马', '奥迪', '丰田', '斯巴鲁']
print(cars)

cars.reverse()
print(cars)

#摩托车 = ['本田', '雅马哈', '铃木', '杜卡迪']

motorcycles = ['本田', '雅马哈', '铃木', '杜卡迪']
print(motorcycles)

too_expensive = '杜卡迪'
motorcycles.remove(too_expensive)

print(motorcycles)
print(f"\nA {too_expensive.title()} 对我来说太贵了。")
