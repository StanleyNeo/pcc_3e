# 10-8_cats_and_dogs 文件和异常 猫和狗 20250625 Stanley Neo

from pathlib import Path

# 要读取的文件列表
文件列表 = ['cats.txt', 'dogs.txt']

for 文件名 in 文件列表:
    print(f"\n正在读取文件: {文件名}")

    # 创建文件路径对象
    文件路径 = Path(文件名)

    try:
        # 尝试读取文件内容
        内容 = 文件路径.read_text(encoding='utf-8')  # 添加编码参数支持中文
    except FileNotFoundError:
        # 文件不存在时的处理
        print("  抱歉，找不到该文件。")
    else:
        # 成功读取文件时打印内容
        print(内容)

from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")

    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")
    else:
        print(contents)