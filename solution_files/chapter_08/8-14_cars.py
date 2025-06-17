# 8-14_cars 函数 汽车信息 20250617 Stanley Neo

def 创建汽车信息(制造商, 型号, **可选配置):
    """
    构建包含汽车完整信息的字典

    参数:
        制造商 (str): 汽车制造商
        型号 (str): 汽车型号
        **可选配置: 任意数量的关键字参数(汽车配置信息)

    返回:
        dict: 包含汽车完整信息的字典
    """
    汽车 = {
        '制造商': 制造商.title(),
        '型号': 型号.title(),
    }

    # 添加可选配置项
    汽车.update(可选配置)

    return 汽车


# 创建汽车信息示例
我的越野车 = 创建汽车信息('斯巴鲁', '傲虎',
                          颜色='蓝色',
                          拖车包=True,
                          驱动方式='全时四驱')

我的老轿车 = 创建汽车信息('本田', '雅阁',
                          生产年份=1991,
                          颜色='白色',
                          大灯类型='弹出式')

# 打印结果
print("【我的越野车】")
for 配置项, 值 in 我的越野车.items():
    print(f"{配置项}: {值}")

print("\n【我的老轿车】")
for 配置项, 值 in 我的老轿车.items():
    print(f"{配置项}: {值}")


# 扩展功能：汽车信息导出
def 导出汽车信息(汽车字典, 文件名='汽车信息.txt'):
    """将汽车信息导出到文件"""
    with open(文件名, 'w', encoding='utf-8') as 文件:
        for 键, 值 in 汽车字典.items():
            文件.write(f"{键}: {值}\n")
    print(f"\n汽车信息已导出到 {文件名}")


导出汽车信息(我的越野车)

def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)
