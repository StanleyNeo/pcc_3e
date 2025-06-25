# 10-9_silent_cats_and_dogs 文件和异常 静默处理缺失文件的猫狗 20250625 Stanley Neo

from pathlib import Path

# 要读取的文件列表
文件列表 = ['cats.txt', 'dogs.txt']

for 文件名 in 文件列表:
    # 创建文件路径对象
    文件路径 = Path(文件名)

    try:
        # 尝试读取文件内容(使用UTF-8编码)
        内容 = 文件路径.read_text(encoding='utf-8')
        print(f"\n{文件名}的内容:")
        print(内容)
    except FileNotFoundError:
        # 静默处理文件不存在的情况(不显示任何错误信息)
        pass