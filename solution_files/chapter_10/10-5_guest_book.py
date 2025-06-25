# 10-5_guest_book 文件和异常 访客记录20250625 Stanley Neo

from pathlib import Path

# 定义访客记录文件路径
文件路径 = Path('guest_book.txt')

# 设置用户输入提示
提示信息 = "\n您好，请问您叫什么名字？"
提示信息 += "\n(如果最后一位客人已登记，请输入'quit') "

# 初始化访客名单
访客名单 = []

while True:
    # 获取用户输入
    姓名 = input(提示信息)

    # 检查是否结束输入
    if 姓名 == 'quit':
        break

    # 反馈并记录访客信息
    print(f"谢谢{姓名}，我们已将您加入访客名单。")
    访客名单.append(姓名)

# 构建文件内容字符串(每个姓名后加换行符)
文件内容 = ''
for 姓名 in 访客名单:
    文件内容 += f"{姓名}\n"

# 将内容写入文件
文件路径.write_text(文件内容, encoding='utf-8')  # 添加编码参数支持中文

print("\n访客名单已更新保存至guest_book.txt文件。")

from pathlib import Path

path = Path('guest_book.txt')

prompt = "\nHi, what's your name? "
prompt += "\nEnter 'quit' if you're the last guest. "

guest_names = []
while True:
    name = input(prompt)
    if name == 'quit':
        break

    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)