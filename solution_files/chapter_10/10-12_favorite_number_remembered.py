# 10-12_favorite_number_remembered 文件和异常 记忆喜欢的数字 20250625 Stanley Neo
# favorite number remembered
# 记忆喜欢的数字

from pathlib import Path
import json

# 定义存储文件路径
文件路径 = Path('favorite_number.json')

try:
    # 尝试读取已存储的数字
    文件内容 = 文件路径.read_text(encoding='utf-8')
except FileNotFoundError:
    # 如果文件不存在，询问并存储新数字
    喜欢的数字 = input("你最喜欢的数字是什么？ ")
    文件内容 = json.dumps(喜欢的数字, ensure_ascii=False)
    文件路径.write_text(文件内容, encoding='utf-8')
    print("谢谢，我会记住这个数字的。")
else:
    # 如果文件存在，显示已存储的数字
    喜欢的数字 = json.loads(文件内容)
    print(f"我知道你最喜欢的数字！它是 {喜欢的数字}。")

from pathlib import Path
import json

path = Path('favorite_number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thanks, I'll remember that.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")