# 8-5_cities 函数 城市  20250617 Stanley Neo

def 描述城市(城市名称, 所在国家='智利'):
    """描述城市及其所属国家"""
    信息 = f"{城市名称.title()} 位于 {所在国家.title()}。"
    print(信息)

# 测试函数
描述城市('圣地亚哥')  # 使用默认国家参数
描述城市('雷克雅未克', '冰岛')  # 提供全部参数
描述城市('蓬塔阿雷纳斯')  # 再次使用默认国家

print("\n----- English Code -----")

def describe_city(city, country='chile'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')
