# 9-6_ice_cream_stand 类和对象 冰淇淋摊 20250618 Stanley Neo

class 餐厅:
    """表示餐厅的类"""

    def __init__(self, 名称, 菜系类型):
        """初始化餐厅属性"""
        self.名称 = 名称.title()
        self.菜系类型 = 菜系类型
        self.服务人数 = 0

    def 描述餐厅(self):
        """打印餐厅描述信息"""
        信息 = f"{self.名称} 提供美味的 {self.菜系类型}。"
        print(f"\n{信息}")

    def 营业中(self):
        """打印餐厅营业信息"""
        信息 = f"{self.名称} 正在营业，欢迎光临！"
        print(f"\n{信息}")

    def 设置服务人数(self, 人数):
        """设置餐厅服务人数"""
        self.服务人数 = 人数

    def 增加服务人数(self, 新增人数):
        """增加餐厅服务人数"""
        self.服务人数 += 新增人数


class 冰淇淋摊(餐厅):
    """表示冰淇淋摊的类，继承自餐厅类"""

    def __init__(self, 名称, 菜系类型='冰淇淋'):
        """初始化冰淇淋摊"""
        super().__init__(名称, 菜系类型)
        self.口味列表 = []

    def 展示口味(self):
        """展示可用的冰淇淋口味"""
        print("\n我们有以下口味可供选择：")
        for 口味 in self.口味列表:
            print(f"- {口味.title()}")


# 创建冰淇淋摊实例
大冰淇淋摊 = 冰淇淋摊('The Big One')
大冰淇淋摊.口味列表 = ['香草', '巧克力', '黑樱桃']

大冰淇淋摊.描述餐厅()
大冰淇淋摊.展示口味()
class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()