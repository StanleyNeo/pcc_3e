# 8-11_archived_messages  函数 已存档消息 20250617 Stanley Neo

def 显示消息(消息列表):
    """显示所有待发送的消息"""
    print("\n【当前待发消息】")
    for 序号, 消息 in enumerate(消息列表, 1):
        print(f"{序号}. {消息}")


def 发送消息(原始列表, 已发列表):
    """
    发送消息并保留原始列表(使用副本)

    参数:
        原始列表 (list): 要发送的消息列表(保留原件)
        已发列表 (list): 存储已发送消息的列表
    """
    待发副本 = 原始列表[:]  # 创建消息副本

    print("\n【开始发送消息】")
    while 待发副本:
        当前消息 = 待发副本.pop(0)  # 从前往后发送
        print(f"↳ 已发送：{当前消息}")
        已发列表.append(当前消息)

    print("✓ 所有消息发送完成")


# 初始化消息
原始消息 = ["你好，项目进展如何？", "请查收附件", "会议改到下午3点 :)"]
已发送消息 = []

# 显示原始消息
显示消息(原始消息)

# 发送消息(保留原始列表)
发送消息(原始消息, 已发送消息)

# 验证结果
print("\n【最终状态】")
print(f"原始消息(保留)：{原始消息}")
print(f"已发送消息：{已发送消息}")


# 新增消息统计功能
def 统计消息(消息列表):
    """显示消息统计信息"""
    print(f"\nℹ️ 消息统计：共 {len(消息列表)} 条")
    if 消息列表:
        平均长度 = sum(len(msg) for msg in 消息列表) / len(消息列表)
        print(f"平均长度：{平均长度:.1f} 字符")


统计消息(已发送消息)

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
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
