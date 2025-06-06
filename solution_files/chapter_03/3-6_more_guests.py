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
print(guests)

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