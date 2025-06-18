# 9-7_admin 类和对象 管理员 20250618 Stanley Neo

class 用户:
    """表示一个简单的用户资料"""

    def __init__(self, 名, 姓, 用户名, 邮箱, 所在地):
        """初始化用户属性"""
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


class 管理员(用户):
    """具有管理员权限的用户"""

    def __init__(self, 名, 姓, 用户名, 邮箱, 所在地):
        """初始化管理员"""
        super().__init__(名, 姓, 用户名, 邮箱, 所在地)
        self.权限列表 = []

    def 显示权限(self):
        """显示该管理员拥有的权限"""
        print("\n管理员权限:")
        for 权限 in self.权限列表:
            print(f"- {权限}")


# 创建管理员实例
eric = 管理员('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.描述用户()

# 设置管理员权限
eric.权限列表 = [
    '可以重置密码',
    '可以管理讨论区',
    '可以暂停账户',
]

eric.显示权限()

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


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

eric.show_privileges()