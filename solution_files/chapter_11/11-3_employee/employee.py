# 11-3_employee 测试代码 雇员加薪类 20250626 Stanley Neo
# employee

# 11-3_employee 测试代码 雇员加薪 20250626 Stanley Neo
# 雇员类

class 雇员:
    """表示雇员的类"""

    def __init__(self, 名, 姓, 薪资):
        """初始化雇员属性"""
        self.名 = 名.title()
        self.姓 = 姓.title()
        self.薪资 = 薪资

    def 加薪(self, 加薪金额=5000):
        """给雇员加薪"""
        self.薪资 += 加薪金额

class Employee:
    """A class to represent an 11-3_employee."""

    def __init__(self, f_name, l_name, salary):
        """Initialize the 11-3_employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the 11-3_employee a raise."""
        self.salary += amount