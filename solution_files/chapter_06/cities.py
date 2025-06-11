# 中国城市数据 20250611 SKNEO

城市数据 = {
    '昆明': {
        '国家': '中国',
        '人口': 8_460_000,
        '附近山脉': '横断山脉',
    },
    '漠河': {
        '国家': '中国',
        '人口': 5_400,
        '附近山脉': '大兴安岭',
    },
    '拉萨': {
        '国家': '中国',
        '人口': 867_900,
        '附近山脉': '喜马拉雅山脉',
    }
}

print("\n=== 中国城市数据（中文）===")
print(城市数据 )

for 城市, 信息 in 城市数据.items():
    print(f"\n{城市}位于{信息['国家']}。")
    print(f"  人口：{信息['人口']}人")
    print(f"  附近山脉：{信息['附近山脉']}")
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {mountains} mounats are nearby.")

