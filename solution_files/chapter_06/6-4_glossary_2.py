# 6-3_编程术语 20250611 SKNEO
编程术语词典 = {
    '字符串': '一系列字符组成的序列',
    'string': 'A series of characters.',
    '注释': '程序中Python解释器会忽略的说明文字',
    'comment': 'A note in a program that the Python interpreter ignores.',
    '列表': '按特定顺序排列的元素集合',
    '循环': '对集合中的每个元素逐个处理的过程',
    '字典': '由键值对组成的数据结构',
    '键': '字典中键值对的第一个元素',
    '值': '字典中与键相关联的数据',
    '条件判断': '对两个值进行比较的表达式',
    '浮点数': '包含小数部分的数值',
    '布尔表达式': '结果为真或假的逻辑表达式',
}

# for key, value in Dictionary.items()
for 术语, 解释 in 编程术语词典.items(): #术语:key 解释:value
    print(f"\n{术语}: {解释}")

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
