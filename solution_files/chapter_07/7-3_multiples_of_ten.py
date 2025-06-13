# 7-3_multiples_of_ten.py
# 7-3_十的倍数判断 20250613 SKNEO

数字 = input("请输入一个数字：")
数字 = int(数字)

if 数字 % 10 == 0:
    print(f"{数字}是10的倍数。")
else:
    print(f"{数字}不是10的倍数。")

number = input("Give me a number, please: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
