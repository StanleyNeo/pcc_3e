# 9-16_login_attempt 类和对象 登录尝试 20250618 Stanley Neo
'''
9-16. Python Module of the Week: One excellent resource for exploring the Python standard library 
is a site called Python Module of the Week. Go to https://pymotw.com and look at the table of contents. 
Find a module that looks interesting to you and read about it, perhaps starting with the random module
'''
'''
9-16. Python 模块周：探索 Python 标准库的一个优秀资源是 Python Module of the Week 网站。
访问 https://pymotw.com 查看目录，找到一个你感兴趣的模块并阅读相关内容，
可以从 random 模块开始。
'''

class 用户:
    """表示一个简单的用户资料"""

    def __init__(self, 名, 姓, 用户名, 邮箱, 所在地):
        """初始化用户"""
        self.名 = 名.title()
        self.姓 = 姓.title()
        self.用户名 = 用户名
        self.邮箱 = 邮箱
        self.所在地 = 所在地.title()
        self.登录尝试次数 = 0

    def 描述用户(self):
        """显示用户信息摘要"""
        print(f"\n{self.名} {self.姓}")
        print(f"  用户名: {self.用户名}")
        print(f"  邮箱: {self.邮箱}")
        print(f"  所在地: {self.所在地}")

    def 问候用户(self):
        """向用户显示个性化问候"""
        print(f"\n欢迎回来, {self.用户名}!")

    def 增加登录尝试(self):
        """增加登录尝试次数"""
        self.登录尝试次数 += 1

    def 重置登录尝试(self):
        """将登录尝试次数重置为0"""
        self.登录尝试次数 = 0

# 创建用户实例
eric = 用户('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.描述用户()
eric.问候用户()

# 测试登录尝试功能
print("\n进行3次登录尝试...")
eric.增加登录尝试()
eric.增加登录尝试()
eric.增加登录尝试()
print(f"  登录尝试次数: {eric.登录尝试次数}")

print("重置登录尝试次数...")
eric.重置登录尝试()
print(f"  登录尝试次数: {eric.登录尝试次数}")

class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f"  Login attempts: {eric.login_attempts}")

print("Resetting login attempts...")
eric.reset_login_attempts()
print(f"  Login attempts: {eric.login_attempts}")