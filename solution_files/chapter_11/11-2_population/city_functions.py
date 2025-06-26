# 11-2_city_functions 测试代码 城市和国家人口 20250626 Stanley Neo
# population

# 11-2_city_functions 测试代码 城市和国家人口 20250626 Stanley Neo
# 人口参数
"""用于处理城市相关功能的函数集合"""

def 城市国家人口(城市名, 国家名, 人口数):
    """返回格式为'城市名, 国家名 - population 人口数'的字符串"""
    输出字符串 = f"{城市名.title()}, {国家名.title()}"
    输出字符串 += f" - population {人口数}"
    return 输出字符串

"""A collection of functions for working with cities."""

def city_country(city, country, population):
    """Return a string like 'Santiago, Chile - 11-2_population 5000000'."""
    output_string = f"{city.title()}, {country.title()}"
    output_string += f" - population {population}"
    return output_string