# 7-4_披萨配料选择 20250613 SKNEO

print("\n=== 披萨配料选择 ===")

配料列表 = []
while True:
    配料 = input("请输入配料名称（输入'完成'结束）：")
    if 配料 == '完成':
        break
    print(f"  正在为您添加配料：{配料}")
    配料列表.append(配料)

print("\n您的披萨将包含以下配料：")
for 配料 in 配料列表:
    print(f"- {配料}")

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break
