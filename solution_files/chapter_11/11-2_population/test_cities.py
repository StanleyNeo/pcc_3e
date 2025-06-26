# 11-2_city_functions 测试代码 测试城市和国家加人口 20250626 Stanley Neo
# test add population

# 11-2_city_functions 测试代码 测试城市国家加人口 20250626 Stanley Neo
# 测试添加人口参数

from city_functions import 城市国家人口

def 测试基础城市国家函数():
    """测试基础的城市国家组合是否能正常工作"""
    圣地亚哥_智利 = 城市国家('santiago', 'chile')
    assert 圣地亚哥_智利 == 'Santiago, Chile'
    print("基础城市国家测试通过！")

from city_functions import city_country

def test_city_country():
    """Does a simple city and country pair work?"""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'

from city_functions_pop_optional import 城市国家

def 测试带人口的函数():
    """测试包含人口参数的情况"""
    # 测试带人口参数
    圣地亚哥_智利 = 城市国家人口('santiago', 'chile', 人口数=5_000_000)
    assert 圣地亚哥_智利 == 'Santiago, Chile - 人口 5000000'

    # 测试不带人口参数
    新加坡 = 城市国家人口('singapore', 'singapore')
    assert 新加坡 == 'Singapore, Singapore'

    print("带人口参数的城市国家测试通过！")

# 运行测试
测试基础城市国家函数()
测试带人口的函数()

from city_functions_pop_optional import city_country

def test_city_country_population():
    """Can I include a 11-2_population argument?"""
    santiago_chile = city_country('santiago', 'chile', population=5_000_000)
    assert santiago_chile == 'Santiago, Chile - population 5000000'