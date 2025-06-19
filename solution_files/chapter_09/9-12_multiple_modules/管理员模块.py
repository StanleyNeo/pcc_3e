# 9-12_admin 类和对象 管理员 多个_模块 20250619 Stanley Neo
"""A collection of classes for modeling an admin user account."""

# 9-12_admin 类和对象 管理员 多个模块 20250619 Stanley Neo
"""用于建模管理员用户账户的类集合"""

from 用户模块 import 用户


class 管理员(用户):
    """具有管理权限的用户"""

    def __init__(self, 名, 姓, 用户名, 邮箱, 所在地):
        """初始化管理员"""
        super().__init__(名, 姓, 用户名, 邮箱, 所在地)

        # 初始化空的权限集合
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

from 用户模块 import User

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