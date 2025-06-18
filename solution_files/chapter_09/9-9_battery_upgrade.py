# 9-9_battery_upgrade 类和对象 升级电池 20250618 Stanley Neo

class 汽车:
    """一个表示汽车的简单尝试"""

    def __init__(self, 制造商, 型号, 年份):
        """初始化描述汽车的属性"""
        self.制造商 = 制造商
        self.型号 = 型号
        self.年份 = 年份
        self.里程表读数 = 0

    def 获取描述性名称(self):
        """返回格式整洁的描述性名称"""
        完整名称 = f"{self.年份} {self.制造商} {self.型号}"
        return 完整名称.title()

    def 读取里程表(self):
        """打印一条显示汽车里程的语句"""
        print(f"这辆车已经行驶了 {self.里程表读数} 公里。")

    def 更新里程表(self, 里程数):
        """将里程表读数设置为给定值"""
        if 里程数 >= self.里程表读数:
            self.里程表读数 = 里程数
        else:
            print("你不能把里程表往回调！")

    def 增加里程数(self, 公里数):
        """将给定量增加到里程表读数"""
        self.里程表读数 += 公里数


class 电池:
    """电动车电池的简单模型"""

    def __init__(self, 电池容量=40):
        """初始化电池属性"""
        self.电池容量 = 电池容量

    def 描述电池(self):
        """打印描述电池容量的语句"""
        print(f"这辆车配备了一个 {self.电池容量}-千瓦时的电池。")

    def 获取续航里程(self):
        """打印电池续航里程的估计值"""
        if self.电池容量 == 40:
            续航里程 = 150
        elif self.电池容量 == 65:
            续航里程 = 225

        print(f"这辆车充满电后大约可以行驶 {续航里程} 公里。")

    def 升级电池(self):
        """如果可能的话升级电池容量"""
        if self.电池容量 == 40:
            self.电池容量 = 65
            print("已将电池升级至65千瓦时。")
        else:
            print("电池已经是最新版本了。")


class 电动车(汽车):
    """电动车的独特之处"""

    def __init__(self, 制造商, 型号, 年份):
        """
        先初始化父类属性
        然后初始化电动车特有属性
        """
        super().__init__(制造商, 型号, 年份)
        self.电池 = 电池()


print("制造一辆电动车，并检查续航里程:")
我的电动车 = 电动车('日产', 'Leaf', 2024)
我的电动车.电池.获取续航里程()

print("\n升级电池后，再次检查续航里程:")
我的电动车.电池.升级电池()
我的电动车.电池.获取续航里程()

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 40:
            self.battery_size = 65
            print("Upgraded the battery to 65 kWh.")
        else:
            print("The battery is already upgraded.")
    
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


print("Make an electric car, and check the range:")
my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.battery.get_range()

print("\nUpgrade the battery, and check the range again:")
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()