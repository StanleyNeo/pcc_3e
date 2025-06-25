# 10-13_user_dictionary 文件和异常 用户信息字典 20250625 Stanley Neo
# user dictionary
# 用户信息存储

from pathlib import Path
import json


def 获取存储的用户信息(文件路径):
    """如果存在则获取存储的用户信息"""
    if 文件路径.exists():
        内容 = 文件路径.read_text(encoding='utf-8')
        用户字典 = json.loads(内容)
        return 用户字典
    else:
        return None


def 获取新用户信息(文件路径):
    """从新用户获取信息"""
    用户名 = input("请问您叫什么名字？ ")
    喜欢的游戏 = input("您最喜欢的游戏是什么？ ")
    喜欢的动物 = input("您最喜欢的动物是什么？ ")

    用户字典 = {
        '用户名': 用户名,
        '游戏': 喜欢的游戏,
        '动物': 喜欢的动物,
    }

    内容 = json.dumps(用户字典, ensure_ascii=False)
    文件路径.write_text(内容, encoding='utf-8')
    return 用户字典


def 问候用户():
    """根据存储的信息问候用户"""
    文件路径 = Path('user_info.json')
    用户字典 = 获取存储的用户信息(文件路径)

    if 用户字典:
        print(f"欢迎回来, {用户字典['用户名']}!")
        print(f"希望您最近玩过 {用户字典['游戏']}。")
        print(f"最近见过 {用户字典['动物']} 吗?")
    else:
        用户字典 = 获取新用户信息(文件路径)
        消息 = f"{用户字典['用户名']}，我们会记住您的信息，欢迎下次再来！"
        print(消息)


问候用户()

from pathlib import Path
import json


def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_user_info(path):
    """Get information from a new user."""
    username = input("What is your name? ")
    game = input("What's your favorite game? ")
    animal = input("What's your favorite animal? ")

    user_dict = {
        'username': username,
        'game': game,
        'animal': animal,
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    """Greet the user by name, and state what we know about them."""
    path = Path('user_info1.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"Hope you've been playing some {user_dict['game']}. ")
        print(f"Have you seen a {user_dict['animal']} recently?")
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you when you return, {user_dict['username']}!"
        print(msg)

greet_user()