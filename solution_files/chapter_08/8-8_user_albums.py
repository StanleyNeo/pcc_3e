# 8-8_user_albums 函数 用户创建专辑 20250617 Stanley Neo

def 创建专辑信息(歌手名, 专辑名, 歌曲数=0):
    """
    构建包含专辑信息的字典

    参数:
        歌手名 (str): 表演者姓名
        专辑名 (str): 专辑名称
        歌曲数 (int): 专辑包含的歌曲数量(可选)

    返回:
        dict: 包含标准化专辑信息的字典
    """
    专辑 = {
        '歌手': 歌手名.strip().title(),
        '专辑': 专辑名.strip().title(),
    }

    # 如果提供了歌曲数量则添加
    if 歌曲数 > 0:
        专辑['歌曲数量'] = 歌曲数

    return 专辑


# 设置交互提示信息
专辑提示 = "\n请输入专辑名称："
歌手提示 = "请输入歌手名："
歌曲数提示 = "请输入歌曲数量(可选，直接回车跳过)："

# 用户引导信息
print("=== 专辑信息收集系统 ===")
print("提示：输入'退出'可随时结束程序\n")

while True:
    # 获取专辑信息
    专辑名 = input(专辑提示)
    if 专辑名.lower() == '退出':
        break

    歌手名 = input(歌手提示)
    if 歌手名.lower() == '退出':
        break

    # 获取可选信息
    歌曲数 = input(歌曲数提示)
    if 歌曲数.lower() == '退出':
        break
    歌曲数 = int(歌曲数) if 歌曲数.isdigit() else 0

    # 创建并显示专辑信息
    专辑信息 = 创建专辑信息(歌手名, 专辑名, 歌曲数)
    print("\n收集到的专辑信息：")
    for 键, 值 in 专辑信息.items():
        print(f"- {键}: {值}")
    print("-" * 30)

print("\n感谢使用专辑信息收集系统！")

def make_album(artist, title, num_songs=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if num_songs:
        album_dict['num_songs'] = num_songs
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")
