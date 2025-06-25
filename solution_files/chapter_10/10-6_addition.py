# 10-6_guest 文件和异常 加法 20250625 Stanley Neo

try:
    # 尝试获取并转换第一个数字
    x = input("请输入第一个数字: ")
    x = int(x)

    # 尝试获取并转换第二个数字
    y = input("请输入第二个数字: ")
    y = int(y)

except ValueError:
    # 处理非数字输入错误
    print("错误：请输入有效的数字！")
else:
    # 计算并输出结果
    总和 = x + y
    print(f"{x} 和 {y} 的和是 {总和}。")

try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("Sorry, I really needed a number.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")