# 9-2_three_restaurants 类和对象 三家餐厅 20250618 Stanley Neo

class 餐厅:
    """表示餐厅的类"""

    def __init__(self, 名称, 菜系类型):
        """初始化餐厅属性"""
        self.名称 = 名称.title()
        self.菜系类型 = 菜系类型

    def 描述餐厅(self):
        """打印餐厅描述信息"""
        信息 = f"{self.名称} 提供美味的 {self.菜系类型}。"
        print(f"\n{信息}")

    def 营业中(self):
        """打印餐厅营业信息"""
        信息 = f"{self.名称} 正在营业，欢迎光临！"
        print(f"\n{信息}")


# 创建三个餐厅实例
披萨店 = 餐厅('the mean queen', 'pizza')
披萨店.描述餐厅()

海鲜餐厅 = 餐厅("ludvig's bistro", 'seafood')
海鲜餐厅.描述餐厅()

泰国餐厅 = 餐厅('mango thai', 'thai food')
泰国餐厅.描述餐厅()

class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()
