favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")

favorite_pizzas = ['意大利辣香肠', '夏威夷', '素食']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("肉食爱好者的")
friend_pizzas.append('香蒜酱')

print("我最喜欢的披萨是：")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print("\n我朋友最喜欢的披萨是：")
for pizza in friend_pizzas:
    print(f"- {pizza}")