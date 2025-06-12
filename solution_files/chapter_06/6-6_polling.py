# 6-6_参与我们的调查 20250611 SKNEO 字典

喜欢的编程语言 = {
    '小美': 'Python',
    '晓丽': 'C',
    '大明': 'Ruby',
    '志强': 'Python',
}

# 打印所有已调查者的偏好
for 姓名, 语言 in 喜欢的编程语言.items():
    print(f"{姓名}最喜欢的编程语言是{语言}。")

print("\n")

# 检查程序员调查情况
程序员名单 = ['志强', '建国', '大卫', '贝卡', '晓丽', '马特', '丹妮']
for 程序员 in 程序员名单:
    if 程序员 in 喜欢的编程语言.keys():
        print(f"感谢{程序员}参与我们的调查！")
    else:
        print(f"{程序员}，请问你最喜欢的编程语言是什么？")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"{coder.title()}, what's your favorite programming language?")
