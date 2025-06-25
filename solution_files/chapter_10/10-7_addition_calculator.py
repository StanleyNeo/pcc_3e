# 10-6_addition 文件和异常 加法 20250625 Stanley Neo

print("输入'q'可随时退出程序。\n")

while True:
    try:
        # 获取第一个数字输入
        第一个数字 = input("\n请输入第一个数字: ")
        if 第一个数字 == 'q':
            break
        第一个数字 = int(第一个数字)

        # 获取第二个数字输入
        第二个数字 = input("请输入第二个数字: ")
        if 第二个数字 == 'q':
            break
        第二个数字 = int(第二个数字)

    except ValueError:
        # 处理非数字输入错误
        print("错误：请输入有效的数字！")
    else:
        # 计算并输出结果
        和 = 第一个数字 + 第二个数字
        print(f"{第一个数字} 加 {第二个数字} 的和是 {和}。")
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break
        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")