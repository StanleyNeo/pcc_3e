# 9-13_dice 类和对象 骰子 20250619 Stanley Neo

# 9-13_dice 类和对象 骰子 20250619 Stanley Neo

from random import randint

class 骰子:
    """表示一个可投掷的骰子"""

    def __init__(self, 面数=6):
        """初始化骰子属性"""
        self.面数 = 面数

    def 投掷(self):
        """返回1到面数之间的随机数"""
        return randint(1, self.面数)

# 创建一个6面骰子，并展示10次投掷结果
六面骰 = 骰子()

结果 = []
for 投掷次数 in range(10):
    单次结果 = 六面骰.投掷()
    结果.append(单次结果)
print("6面骰10次投掷结果:")
print(结果)

# 创建一个10面骰子，并展示10次投掷结果
十面骰 = 骰子(面数=10)

结果 = []
for 投掷次数 in range(10):
    单次结果 = 十面骰.投掷()
    结果.append(单次结果)
print("\n10面骰10次投掷结果:")
print(结果)

# 创建一个20面骰子，并展示10次投掷结果
二十面骰 = 骰子(面数=20)

结果 = []
for 投掷次数 in range(10):
    单次结果 = 二十面骰.投掷()
    结果.append(单次结果)
print("\n20面骰10次投掷结果:")
print(结果)

from random import randint

class Die:
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)