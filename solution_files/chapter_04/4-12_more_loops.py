my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")

my_foods = ['披萨', '沙拉三明治', '胡萝卜蛋糕']
friend_foods = my_foods[:]

my_foods.append('奶油卷')
friend_foods.append('冰淇淋')

print("我最喜欢的食物是：")
for food in my_foods:
    print(f"- {food}")

print("\n我朋友最喜欢的食物是：")
for food in friend_foods:
    print(f"- {food}")