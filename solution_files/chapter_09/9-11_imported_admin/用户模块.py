# 9-11_my_user 导入管理员 类和对象 我的用户 20250619 Stanley Neo
"""A collection of classes for modeling users."""

# 9-11_my_user 类和对象 我的用户 20250619 Stanley Neo
"""用于建模用户的类集合"""


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

        # 初始化权限集合
        self.权限 = 权限()


class 权限:
    """存储管理员权限的类"""

    def __init__(self, 权限列表=[]):
        self.权限列表 = 权限列表

    def 显示权限(self):
        print("\n权限列表:")
        if self.权限列表:
            for 权限 in self.权限列表:
                print(f"- {权限}")
        else:
            print("- 该用户暂无任何权限")

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
        
        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")