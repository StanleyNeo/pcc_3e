# 8-4_large_shirts 函数 大号衬衫 20250616 SKNEO

def 制作T恤(尺码='大号', 文字内容='我爱Python!'):
    """显示将要制作的T恤信息"""
    print(f"\n我将制作一件{尺码}号的T恤衫。")
    print(f'T恤上将会印着："{文字内容}"')

# 测试函数
制作T恤()  # 使用全部默认参数
制作T恤(尺码='中号')  # 修改尺码，使用默认文字
制作T恤('小号', '程序员都是天才！')  # 修改全部参数

def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')
