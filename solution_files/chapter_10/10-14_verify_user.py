# 10-14_verify_user 文件和异常 验证用户 20250625 Stanley Neo
# 验证用户身份

from pathlib import Path
import json


def 获取存储的用户名(文件路径):
    """如果存在则获取存储的用户名"""
    if 文件路径.exists():
        内容 = 文件路径.read_text(encoding='utf-8')
        用户名 = json.loads(内容)
        return 用户名
    else:
        return None


def 获取新用户名(文件路径):
    """提示输入新用户名"""
    用户名 = input("请问您叫什么名字？ ")
    内容 = json.dumps(用户名, ensure_ascii=False)
    文件路径.write_text(内容, encoding='utf-8')
    return 用户名


def 问候用户():
    """验证并问候用户"""
    文件路径 = Path('username.json')
    用户名 = 获取存储的用户名(文件路径)

    if 用户名:
        # 验证用户身份
        验证结果 = input(f"您是 {用户名} 吗？(y/n) ")
        if 验证结果.lower() == 'y':
            print(f"欢迎回来, {用户名}!")
        else:
            用户名 = 获取新用户名(文件路径)
            print(f"{用户名}，我们会记住您，欢迎下次再来！")
    else:
        用户名 = 获取新用户名(文件路径)
        print(f"{用户名}，我们会记住您，欢迎下次再来！")


问候用户()

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")    
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()