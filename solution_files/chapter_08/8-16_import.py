# 8-16_import 函数 导入方式 20250618 Stanley Neo
# 我将使用一个简单的问候函数来演示不同的导入方式：

# # greeting.py
# """包含问候功能的模块"""
#
# def greet_user(username):
#     """向指定用户发出问候"""
#     print(f"Hello, {username.title()}!")

# output: Hello, Alice!

# main_program.py
"""演示不同导入方式的主程序"""

# 方法1：直接导入模块
import greeting
greeting.greet_user('alice')
# Hello, Alice!

# 方法2：从模块导入特定函数
from greeting import greet_user
greet_user('bob')
# Hello, Bob! # 方法5

# 方法3：导入并使用 别名
from greeting import greet_user as gu
gu('charlie')
# Hello, Charlie!

# 方法4：给模块起别名
import greeting as g
g.greet_user('david')
# Hello, David!

# 方法5：导入所有内容(不推荐)
from greeting import *
greet_user('eve')
# Hello, Eve!  # 方法2