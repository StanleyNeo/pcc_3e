# 9-3_users 类和对象 用户 20250618 Stanley Neo

class 用户:
    """表示一个简单的用户资料"""

    def __init__(self, 名, 姓, 用户名, 邮箱, 所在地):
        """初始化用户"""
        self.名 = 名.title()
        self.姓 = 姓.title()
        self.用户名 = 用户名
        self.邮箱 = 邮箱
        self.所在地 = 所在地.title()

    def 描述用户(self):
        """显示用户信息的摘要"""
        print(f"\n{self.名} {self.姓}")
        print(f"  用户名: {self.用户名}")
        print(f"  邮箱: {self.邮箱}")
        print(f"  所在地: {self.所在地}")

    def 问候用户(self):
        """向用户显示个性化的问候语"""
        print(f"\n欢迎回来, {self.用户名}!")

eric = 用户('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.描述用户()
eric.问候用户()

willie = 用户('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.描述用户()
willie.问候用户()

class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()
