# 9-1_restaurant 类和对象 餐厅 20250618 Stanley Neo

class 餐厅:
    """表示餐厅的类"""

    def __init__(self, 名称, 菜系类型):
        """初始化餐厅"""
        self.名称 = 名称.title()
        self.菜系类型 = 菜系类型

    def 描述餐厅(self):
        """显示餐厅的摘要信息"""
        信息 = f"{self.名称} 提供美味的 {self.菜系类型}。"
        print(f"\n{信息}")

    def 开业状态(self):
        """显示餐厅正在营业的消息"""
        信息 = f"{self.名称} 正在营业。欢迎光临！"
        print(f"\n{信息}")

餐厅实例 = 餐厅('欧洲女王', '比萨')
print(餐厅实例.名称)
print(餐厅实例.菜系类型)

餐厅实例.描述餐厅()
餐厅实例.开业状态()

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

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
