# 8-7_album_num_song 函数 专辑编号歌曲 20250617 Stanley Neo

def 创建专辑(歌手, 专辑名, 歌曲数=0):
    """创建一个包含专辑信息的字典"""
    专辑字典 = {
        '歌手': 歌手.title(),
        '专辑名': 专辑名.title(),
        }
    if 歌曲数:
        专辑字典['歌曲数'] = 歌曲数
    return 专辑字典

专辑 = 创建专辑('metallica', 'ride the lightning')
print(专辑)

专辑 = 创建专辑('beethoven', 'ninth symphony')
print(专辑)

专辑 = 创建专辑('willie nelson', 'red-headed stranger')
print(专辑)

专辑 = 创建专辑('iron maiden', 'piece of mind', 歌曲数=8)
print(专辑)

def make_album(artist, title, num_songs=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if num_songs:
        album_dict['num_songs'] = num_songs
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', num_songs=8)
print(album)
