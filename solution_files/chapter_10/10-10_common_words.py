# 10-10_common_words 文件和异常 常用词 20250625 Stanley Neo

from pathlib import Path

def 统计单词出现次数(文件名, 单词):
    """统计单词在文本中出现的次数"""
    # 注意：这是一个简单近似统计，返回的数字会比实际出现次数多
    文件路径 = Path(文件名)
    try:
        # 使用UTF-8编码读取文件
        文件内容 = 文件路径.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"错误：找不到文件 '{文件名}'")
    except UnicodeDecodeError:
        print(f"错误：无法用UTF-8编码读取 '{文件名}'")
    else:
        # 统计单词出现次数（不区分大小写）
        出现次数 = 文件内容.lower().count(单词.lower())
        结果信息 = f"单词 '{单词}' 在文件 {文件名} 中大约出现了 {出现次数} 次。"
        print(结果信息)

# 使用示例
文件名 = 'alice.txt'
统计单词出现次数(文件名, 'the')

from pathlib import Path

def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    #   will be higher than the actual count.
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except UnicodeDecodeError:
        print(f"Error: Could not read '{filename}' with UTF-8 encoding.")
    else:
        word_count = contents.lower().count(word.lower())
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filename = 'alice.txt'
count_common_words(filename, 'the')