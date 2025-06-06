# 20250606 SKNEO
# 3-9 Dinner Guests

# Invite some people to dinner.
guests = ['guido van rossum', 'jack turner', 'lynn hill']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1, 'gary snyder')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

# Empty out the list.
del(guests[0])          # total [0] [1] del [0] left List [0]
del(guests[0])          # del [0] again will empty the List

# Prove the list is empty.
print(guests)

# 邀请一些人来吃饭。
guests = ['大头', '阿连', '婆婆']

name = guests[0].title()
print(f"{name}, 请来吃晚餐.")

name = guests[1].title()
print(f"{name}, 请来吃晚餐.")

name = guests[2].title()
print(f"{name}, 请来吃晚餐.")

name = guests[1].title()
print(f"\n抱歉，{name} 不能来吃晚餐了.")

# 阿连来不了！我们邀请加里来吧。

del(guests[1])                              # remove guests[1]
guests.insert(1, '加里')      # insert guests[1]

print("\n----- New invitations list -----")
name = guests[0].title()
print(f"{name}, 请来吃晚餐.")

name = guests[1].title()
print(f"{name}, 请来吃晚餐.")

name = guests[2].title()
print(f"{name}, 请来吃晚餐.")

# 我们有一张更大的桌子，所以让我们在名单上添加更多的人。
print("\n我们有一张更大的桌子!")
guests.insert(0, '永明')
guests.insert(2, '郭亮')
guests.append('梁总')
print(guests)

name = guests[0].title()
print(f"{name}, 请来吃晚餐.")

name = guests[1].title()
print(f"{name}, 请来吃晚餐.")

name = guests[2].title()
print(f"{name}, 请来吃晚餐.")

name = guests[3].title()
print(f"{name}, 请来吃晚餐.")

name = guests[4].title()
print(f"{name}, 请来吃晚餐.")

name = guests[5].title()
print(f"{name}, 请来吃晚餐.")

# 哦不，桌子不能准时到达！
print("\n抱歉，我们只能邀请两个人吃饭。")
print(guests)

name = guests.pop()
print(f"抱歉，{name.title()} 桌子上没有空位了。")
print(guests)

name = guests.pop()
print(f"抱歉，{name.title()} 桌子上没有空位了。")
print(guests)

name = guests.pop()
print(f"抱歉，{name.title()} 桌子上没有空位了。")
print(guests)

name = guests.pop()
print(f"抱歉，{name.title()} 桌子上没有空位了。")
print(guests)

# 应该还剩下两个人。我们邀请他们吧。
name = guests[0].title()
print(f"{name}, 请来吃晚餐.")

name = guests[1].title()
print(f"{name}, 请来吃晚餐.")

number_invited = len(guests)
print(f"Number of people we are inviting to dinner is {number_invited} people")