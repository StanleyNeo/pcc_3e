# 9-4_number_served 类和对象 服务人数 20250618 Stanley Neo

class 餐厅:
    """表示餐厅的类"""

    def __init__(self, 名称, 菜系类型):
        """初始化餐厅属性"""
        self.名称 = 名称.title()
        self.菜系类型 = 菜系类型
        self.服务人数 = 0  # 新增服务人数属性，初始值为0

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


# 创建餐厅实例
披萨店 = 餐厅('the mean queen', 'pizza')
披萨店.描述餐厅()

# 测试服务人数功能
print(f"\n已服务人数: {披萨店.服务人数}")
披萨店.服务人数 = 500  # 直接修改属性
print(f"已服务人数: {披萨店.服务人数}")

披萨店.设置服务人数(1000)  # 通过方法修改
print(f"已服务人数: {披萨店.服务人数}")

披萨店.增加服务人数(250)  # 增加服务人数
print(f"已服务人数: {披萨店.服务人数}")


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


restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 500
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1000)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(250)
print(f"Number served: {restaurant.number_served}")