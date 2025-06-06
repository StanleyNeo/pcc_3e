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
del(guests[1])                                      # remove guests[1]
guests.insert(1, 'gary snyder')      # insert guests[1]

print("\n----- New invitations list -----")

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
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