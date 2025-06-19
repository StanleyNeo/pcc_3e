# 9-10_my_restaurant 类和对象 我的餐厅 20250619 Stanley Neo
"""A class representing a restaurant."""

"""表示餐厅的类"""

class 餐厅:
    """表示餐厅的类"""

    def __init__(self, 名称, 菜系类型):
        """初始化餐厅属性"""
        self.名称 = 名称.title()
        self.菜系类型 = 菜系类型
        self.已服务人数 = 0

    def 描述餐厅(self):
        """显示餐厅摘要信息"""
        信息 = f"{self.名称} 提供美味的 {self.菜系类型}。"
        print(f"\n{信息}")

    def 开业状态(self):
        """显示餐厅正在营业的信息"""
        信息 = f"{self.名称} 正在营业，欢迎光临！"
        print(f"\n{信息}")

    def 设置服务人数(self, 人数):
        """设置已服务的顾客人数"""
        self.已服务人数 = 人数

    def 增加服务人数(self, 新增人数):
        """增加已服务的顾客人数"""
        self.已服务人数 += 新增人数

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