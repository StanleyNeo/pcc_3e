# 10-4_guest 文件和异常 用户 20250625 Stanley Neo

from pathlib import Path

# 定义文件路径
文件路径 = Path('guest.txt')

# 获取用户输入
用户名 = input("请问您叫什么名字？ ")

# 将用户名写入文件
文件路径.write_text(用户名, encoding='utf-8')  # 添加编码参数支持中文

print(f"感谢您的来访，{用户名}！您的信息已保存。")

from pathlib import Path

path = Path('guest.txt')

name = input("What's your name? ")
path.write_text(name)