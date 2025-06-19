# 9-14_lottery 类和对象 彩票 20250619 Stanley Neo

# 9-14_lottery 类和对象 彩票 20250619 Stanley Neo

from random import choice

可选项目 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

中奖号码 = []
print("让我们看看中奖号码是什么...")

# 我们不希望中奖号码或字母重复，所以使用while循环
while len(中奖号码) < 4:
    抽取的项目 = choice(可选项目)

    # 只有当抽取的项目不在中奖号码中时才添加
    if 抽取的项目 not in 中奖号码:
        print(f"  我们抽出了一个 {抽取的项目}!")
        中奖号码.append(抽取的项目)

print(f"\n最终的中奖号码是: {中奖号码}")

from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("Let's see what the winning ticket is...")

# We don't want to repeat winning numbers or letters, so we'll use a
#   while loop.
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    # Only add the pulled item to the winning ticket if it hasn't
    #   already been pulled.
    if pulled_item not in winning_ticket:
        print(f"  We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)

print(f"\nThe final winning ticket is: {winning_ticket}")