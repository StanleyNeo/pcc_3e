# 10-1_learning_c 文件和异常 学习C 20250621 Stanley Neo

from pathlib import Path

# 读取文件内容
文件路径 = Path('learning_python.txt')
文件内容 = 文件路径.read_text(encoding='utf-8')  # 添加编码参数支持中文

# 替换Python为C并逐行打印
行列表 = 文件内容.splitlines()
for 行 in 行列表:
    修改后行 = 行.replace('Python', 'C')  # 将Python替换为C
    print(修改后行)

# 字符串替换示例
示例消息 = "I really like dogs."
修改后消息 = 示例消息.replace('dog', 'cat')  # 将dog替换为cat
print("\n字符串替换示例:")
print(修改后消息)

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)

# .replace()
message = "I really like dogs."
message = message.replace('dog', 'cat')
print(message)