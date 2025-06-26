# 11-4_test_employee 测试代码 雇员加薪类 20250626 Stanley Neo
# employee with fixture

import pytest
from employee import 雇员

@pytest.fixture
def 测试员工():
    """创建一个测试用的雇员实例"""
    return 雇员('张', '三', 50000)

def test_默认加薪(测试员工):
    """测试默认加薪功能"""
    测试员工.加薪()
    assert 测试员工.薪资 == 55000

def test_自定义加薪(测试员工):
    """测试自定义加薪金额"""
    测试员工.加薪(10000)
    assert 测试员工.薪资 == 60000

def test_姓名格式化(测试员工):
    """测试姓名自动首字母大写"""
    assert 测试员工.名 == '张'
    assert 测试员工.姓 == '三'

import pytest

from employee import 雇员

@pytest.fixture
def 测试员工():
    """所有测试函数可用的雇员实例"""
    return 雇员('eric', 'matthes', 65_000)

def test_默认加薪(测试员工):
    """测试默认加薪功能"""
    测试员工.加薪()
    assert 测试员工.薪资 == 70_000

def test_自定义加薪(测试员工):
    """测试自定义加薪功能"""
    测试员工.加薪(10000)
    assert 测试员工.薪资 == 75_000

import pytest

from employee import Employee

@pytest.fixture
def employee():
    """An Employee object that will be available to all test functions."""
    employee = Employee('eric', 'matthes', 65_000)
    return employee

def test_give_default_raise(employee):
    """Test that a default raise works correctly."""
    employee.give_raise()
    assert employee.salary == 70_000

def test_give_custom_raise(employee):
    """Test that a custom raise works correctly."""
    employee.give_raise(10000)
    assert employee.salary == 75_000
