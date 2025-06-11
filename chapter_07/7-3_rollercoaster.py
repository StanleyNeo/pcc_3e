

# 获取用户身高输入（单位：厘米）
身高 = input("请问您的身高是多少厘米？ ")
身高 = int(身高)  # 转换为整数

# 判断身高是否符合要求（120厘米为儿童游乐设施常见标准）
if 身高 >= 120:
    print("\n您的身高符合乘坐要求！")
else:
    print("\n您需要再长高一些才能乘坐哦~")

height = input("How tall are you, in inches? ")
height = int(height)

# 添加异常处理：
try:
    身高 = int(input("请问您的身高是多少厘米？ "))
except ValueError:
    print("请输入有效的数字哦！")

# 多条件判断：
if 身高 >= 120:
    print("\n您可以玩所有项目！")
elif 110 <= 身高 < 120:
    print("\n您可以玩部分项目（需家长陪同）")
else:
    print("\n暂不符合乘坐要求")

# 单位选择功能：
单位 = input("请选择单位：1-厘米 2-米 ")
if 单位 == "2":
    身高 = float(input("请输入身高（米）：")) * 100
else:
    身高 = int(input("请输入身高（厘米）："))




if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")