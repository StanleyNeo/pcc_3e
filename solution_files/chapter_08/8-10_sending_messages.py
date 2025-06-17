# 8-10_sending_messages 函数 发送消息 20250617 Stanley Neo

def 显示消息(消息列表):
    """显示所有待发消息"""
    print("\n【待发消息列表】")
    for 消息 in 消息列表:
        print(f" - {消息}")

def 发送消息(待发消息, 已发消息):
    """
    发送所有消息并转移到已发列表
    参数:
        待发消息 (list): 原始消息列表(将被清空)
        已发消息 (list): 存储已发消息的列表
    """
    print("\n【正在发送消息...】")
    while 待发消息:
        当前消息 = 待发消息.pop(0)  # 从前面开始发送
        print(f"正在发送: {当前消息}")
        已发消息.append(当前消息)
    print("所有消息发送完成！")

# 初始化消息列表
待发消息 = ["你好，今天天气如何？", "项目进展顺利吗？", "记得下午3点的会议 :)"]
已发消息 = []

# 显示原始消息
显示消息(待发消息)

# 发送消息
发送消息(待发消息, 已发消息)

# 验证结果
print("\n【最终状态】")
print(f"待发消息: {待发消息}")
print(f"已发消息: {已发消息}")

# 额外功能：消息备份
def 备份消息(消息列表, 文件名):
    """将消息列表保存到文件"""
    with open(文件名, 'w', encoding='utf-8') as 文件:
        for 消息 in 消息列表:
            文件.write(f"{消息}\n")
    print(f"\n消息已备份到 {文件名}")

备份消息(已发消息, 'sent_messages_backup.txt')

def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
