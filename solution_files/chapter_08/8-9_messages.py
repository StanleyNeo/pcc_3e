# 8-9_messages 函数 消息展示 20250617 Stanley Neo

def 显示消息(消息列表, 前缀="", 后缀=""):
    """
    打印列表中的所有消息，可添加前后缀装饰

    参数:
        消息列表 (list): 要显示的消息列表
        前缀 (str): 每条消息前添加的内容(可选)
        后缀 (str): 每条消息后添加的内容(可选)
    """
    print("\n=== 消息展示 ===")  # 添加标题分隔

    for 消息 in 消息列表:
        # 移除首尾空格并格式化输出
        格式化消息 = f"{前缀} {消息.strip()} {后缀}"
        print(格式化消息)

    print("=" * 15)  # 添加结束分隔线


# 基础用法示例
消息集合1 = ["你好啊", "最近怎么样？", "笑脸 :)"]
显示消息(消息集合1)

# 带装饰的用法示例
消息集合2 = ["尊敬的客户", "您的订单已发货", "祝您生活愉快 ^_^"]
显示消息(消息集合2,
         前缀="🔹",
         后缀="🔸")

# 从文件读取消息示例
"""
# messages.txt内容：
早上好
今天天气真好
周末愉快
"""

def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)


messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

print("\n -------------")
messages = ["hello sir", "how are u getting on?", ":-)"]
show_messages(messages)