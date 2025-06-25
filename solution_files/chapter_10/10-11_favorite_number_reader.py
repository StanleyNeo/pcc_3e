# 10-11_favorite_number_reader 文件和异常 读取喜欢的数字 20250625 Stanley Neo
# favorite number reader
# 读取喜欢的数字

from pathlib import Path
import json

# 定义JSON文件路径
文件路径 = Path('favorite_number.json')

try:
    # 读取文件内容(使用UTF-8编码)
    文件内容 = 文件路径.read_text(encoding='utf-8')
    # 解析JSON数据
    喜欢的数字 = json.loads(文件内容)
    print(f"我知道你喜欢的数字！它是 {喜欢的数字}。")

except FileNotFoundError:
    print(f"错误：找不到文件 {文件路径}")
except json.JSONDecodeError:
    print(f"错误：文件 {文件路径} 不是有效的JSON格式")
except Exception as e:
    print(f"发生未知错误: {e}")
from pathlib import Path
import json

path = Path('favorite_number.json')
contents = path.read_text()
number = json.loads(contents)

print(f"I know your favorite number! It's {number}.")