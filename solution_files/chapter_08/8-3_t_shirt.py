# 8-3_t_shirt 函数 制作T恤 20250616 SKNEO

def 制作T恤(尺码, 文字内容):
    """显示将要制作的T恤信息"""
    print(f"\n我将制作一件{尺码}号的T恤衫。")
    print(f'T恤上将会印着："{文字内容}"')

# 调用函数
制作T恤('大号', '我爱Python!')
制作T恤(文字内容="代码可读性很重要", 尺码='中号')

def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')
