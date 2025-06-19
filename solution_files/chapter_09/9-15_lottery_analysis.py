# 9-15_lottery_analysis 类和对象 彩票分析 20250619 Stanley Neo

from random import choice

def 获取中奖号码(可选项目):
    """从可选项目中返回一个中奖号码"""
    中奖号码 = []

    # 我们不希望中奖号码或字母重复，所以使用while循环
    while len(中奖号码) < 4:
        抽取的项目 = choice(可选项目)

        # 只有当抽取的项目不在中奖号码中时才添加
        if 抽取的项目 not in 中奖号码:
            中奖号码.append(抽取的项目)

    return 中奖号码

def 检查号码(玩家号码, 中奖号码):
    # 检查玩家号码中的所有元素，如果有任何一个不在中奖号码中，返回False
    for 元素 in 玩家号码:
        if 元素 not in 中奖号码:
            return False

    # 我们中奖了！
    return True

def 生成随机号码(可选项目):
    """从可选项目中返回一个随机号码"""
    号码 = []
    # 我们不希望号码或字母重复，所以使用while循环
    while len(号码) < 4:
        抽取的项目 = choice(可选项目)

        # 只有当抽取的项目不在号码中时才添加
        if 抽取的项目 not in 号码:
            号码.append(抽取的项目)

    return 号码


可选项目 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
中奖号码 = 获取中奖号码(可选项目)

尝试次数 = 0
是否中奖 = False

# 设置最大尝试次数，防止无限循环
最大尝试次数 = 1_000_000

while not 是否中奖:
    新号码 = 生成随机号码(可选项目)
    是否中奖 = 检查号码(新号码, 中奖号码)
    尝试次数 += 1
    if 尝试次数 >= 最大尝试次数:
        break

if 是否中奖:
    print("恭喜您中奖了！")
    print(f"您的号码: {新号码}")
    print(f"中奖号码: {中奖号码}")
    print(f"仅用了 {尝试次数} 次尝试就中奖了！")
else:
    print(f"尝试了 {尝试次数} 次，没有中奖 :(")
    print(f"您的号码: {新号码}")
    print(f"中奖号码: {中奖号码}")

from random import choice

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a
    #   while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the 
    #   winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")