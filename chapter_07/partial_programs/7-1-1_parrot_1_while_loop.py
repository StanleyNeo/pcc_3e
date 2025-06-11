#
提示信息 = "\n请发言（输入'退出'结束对话）："

while True:
    用户输入 = input(提示信息)

    if 用户输入.lower() == '退出':
        print("对话结束")
        break

    print(f"您说：{用户输入}")

# prompt = "\nTell me something, and I will repeat it back to you:" +
# "\nEnter 'quit' to end the program. "
# 提示信息 = "\n请输入任意内容，我会重复您的话："
# 提示信息 += "\n输入'退出'可结束程序。 "

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)