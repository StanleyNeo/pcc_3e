# 11-2_city_functions_population 测试代码 城市和国家加人口 20250626 Stanley Neo
# add population

"""A collection of functions for working with cities."""

# 11-2_city_functions_population 测试代码 城市国家加人口 20250626 Stanley Neo
# 添加人口参数

"""用于处理城市相关功能的函数集合"""

def 城市国家(城市名, 国家名, 人口数=0):
    """返回表示城市-国家对的字符串"""
    输出字符串 = f"{城市名.title()}, {国家名.title()}"
    if 人口数:
        输出字符串 += f" - 人口 {人口数}"
    return 输出字符串

def city_country(city, country, population=0):
    """Return a string representing a city-country pair."""
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string