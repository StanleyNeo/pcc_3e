# 9-12_my_admin 类和对象 我的管理员 多个模块 20250619 Stanley Neo

from 管理员模块 import 管理员

eric = 管理员('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.描述用户()

eric_权限 = [
    '可以重置密码',
    '可以管理讨论区',
    '可以暂停账户',
]
eric.权限.权限列表 = eric_权限

print(f"\n管理员 {eric.用户名} 拥有以下权限:")
eric.权限.显示权限()

from 管理员模块 import Admin

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges

print(f"\nThe admin {eric.username} has these privileges: ")
eric.privileges.show_privileges()