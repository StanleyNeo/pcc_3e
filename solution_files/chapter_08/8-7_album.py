# 8-7_album 函数 创建专辑 20250617 Stanley Neo

def 创建专辑(歌手姓名, 专辑名称, 发行年份=None):
    """
    构建包含专辑信息的字典

    参数:
        歌手姓名 (str): 歌手的全名
        专辑名称 (str): 专辑名称
        发行年份 (int/None): 可选的发行年份

    返回:
        dict: 包含标准化专辑信息的字典
    """
    专辑信息 = {
        '歌手': 歌手姓名.title(),  # 姓名首字母大写
        '专辑': 专辑名称.title(),  # 专辑名首字母大写
    }

    # 如果有发行年份则添加
    if 发行年份 is not None:
        专辑信息['年份'] = 发行年份

    return 专辑信息


# 测试基础功能
专辑1 = 创建专辑('metallica', 'ride the lightning')
print(专辑1)

# 测试中文输入
专辑2 = 创建专辑('周杰伦', '七里香', 2004)
print(专辑2)

# 测试特殊字符处理
专辑3 = 创建专辑('beyoncé', 'lemonade', 2016)
print(专辑3)

print("\n----- English Code -----")
def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)
