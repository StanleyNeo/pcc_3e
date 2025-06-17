# 8-6_city_names 函数 城市名 20250617 Stanley Neo

def 城市国家(城市名, 国家名):
    """返回格式为'城市名, 国家名'的字符串"""
    return f"{城市名.title()}, {国家名.title()}"

# 测试函数
城市信息 = 城市国家('圣地亚哥', '智利')
print(城市信息)

城市信息 = 城市国家('乌斯怀亚', '阿根廷')
print(城市信息)

城市信息 = 城市国家('朗伊尔城', '斯瓦尔巴群岛')
print(城市信息)

print("\n----- English Code -----")
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)

def 城市国家(城市名, 国家名, 简写=True):
    """支持返回简写格式"""
    if 简写:
        return f"{城市名[:3]}等, {国家名[:3]}"
    return f"{城市名}, {国家名}"

# 测试函数
城市信息 = 城市国家('圣地亚哥', '智利')
print(城市信息)

城市信息 = 城市国家('乌斯怀亚', '阿根廷')
print(城市信息)

城市信息 = 城市国家('朗伊尔城', '斯瓦尔巴群岛')
print(城市信息)