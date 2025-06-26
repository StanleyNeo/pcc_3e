# 11-3_employee 测试代码 测试雇员加薪类 20250626 Stanley Neo
# test employee

# 11-3_employee 测试代码 雇员加薪测试 20250626 Stanley Neo
# 测试雇员类

from employee import 雇员

def 测试默认加薪():
    """测试默认加薪金额是否正确"""
    员工 = 雇员('eric', 'matthes', 65_000)
    员工.加薪()
    assert 员工.薪资 == 70_000
    print("默认加薪测试通过！")

def 测试自定义加薪():
    """测试自定义加薪金额是否正确"""
    员工 = 雇员('eric', 'matthes', 65_000)
    员工.加薪(10000)
    assert 员工.薪资 == 75_000
    print("自定义加薪测试通过！")

# 运行测试
测试默认加薪()
测试自定义加薪()

from employee import Employee

def test_give_default_raise():
    """Test that a default raise works correctly."""
    employee = Employee('eric', 'matthes', 65_000)
    employee.give_raise()
    assert employee.salary == 70_000

def test_give_custom_raise():
    """Test that a custom raise works correctly."""
    employee = Employee('eric', 'matthes', 65_000)
    employee.give_raise(10000)
    assert employee.salary == 75_000
