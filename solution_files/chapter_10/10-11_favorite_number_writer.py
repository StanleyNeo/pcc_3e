# 10-11_favorite_number_writer 文件和异常 喜欢的数字写入程序 20250625 Stanley Neo
# favorite number writer
# 喜欢的数字写入程序

from pathlib import Path
import json

# 获取用户喜欢的数字
喜欢的数字 = input("你最喜欢的数字是什么？ ")

# 准备文件路径
文件路径 = Path('favorite_number.json')

# 将数字转换为JSON格式并写入文件
文件内容 = json.dumps(喜欢的数字, ensure_ascii=False)  # 确保非ASCII字符正常保存
文件路径.write_text(文件内容, encoding='utf-8')  # 使用UTF-8编码保存

print("谢谢！我会记住这个数字的。")

from pathlib import Path
import json

number = input("What's your favorite number? ")

path = Path('favorite_number.json')
contents = json.dumps(number)
path.write_text(contents)

print("Thanks! I'll remember that number.")