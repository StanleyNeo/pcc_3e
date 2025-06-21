# 10-1_learning_python 文件和异常 学习Python 20250621 Stanley Neo

from pathlib import Path

# 读取整个文件内容并打印
print("--- 读取整个文件内容:")
文件路径 = Path('learning_python.txt')
文件内容 = 文件路径.read_text(encoding='utf-8')  # 添加编码参数支持中文
print(文件内容)

# 逐行读取并打印文件内容
print("\n--- 逐行读取文件内容:")
行列表 = 文件内容.splitlines()
for 行 in 行列表:
    print(行)

from pathlib import Path

print("--- Reading in the entire file:")
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

print("\n--- Looping over the lines:")
lines = contents.splitlines()
for line in lines:
    print(line)
