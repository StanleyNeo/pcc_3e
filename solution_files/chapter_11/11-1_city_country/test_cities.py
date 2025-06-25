# 11-1_test_cities 测试代码 测试城市国家 20250625 Stanley Neo

from city_functions import 城市国家


def 测试城市国家函数():
    """测试简单的城市国家组合是否能正常工作"""
    # 测试用例1：普通城市国家组合
    圣地亚哥_智利 = 城市国家('santiago', 'chile')
    assert 圣地亚哥_智利 == 'Santiago, Chile'

    # 测试用例2：包含空格的地区名
    金文泰_新加坡 = 城市国家('clementi', 'singapore')
    assert 金文泰_新加坡 == 'Clementi, Singapore'

    # 测试用例3：多单词城市名
    香港_中国 = 城市国家('hong kong', 'china')
    assert 香港_中国 == 'Hong Kong, China'

    print("所有测试用例通过！")


# 运行测试
测试城市国家函数()

from city_functions import city_country

def test_city_country():
    """Does a simple city and country pair work?"""
    santiago_chile = city_country('santiago', 'chile')
    clementi_singapore = city_country('clementi', 'singapore')
    hongkong_china = city_country('hong kong', 'china')
    assert santiago_chile == 'Santiago, Chile'
    assert clementi_singapore == 'Clementi, Singapore'
    assert hongkong_china == 'Hong Kong, China'