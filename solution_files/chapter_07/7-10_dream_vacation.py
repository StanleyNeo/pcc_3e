# 7-10_dream_vocation 20250613 SKNEO
# 7-10_旅行愿望

print("=== 全球旅行愿望调查 ===")

调查结果 = {}
地区分类 = {
    '国内': ['北京', '上海', '西藏'],
    '亚洲': ['东京', '巴厘岛', '迪拜'],
    '欧美': ['巴黎', '纽约', '罗马']
}

while True:
    # 输入验证
    while True:
        姓名 = input("\n请输入您的姓名：").strip()
        if 姓名:
            break
        print("⚠️ 姓名不能为空！")

    # 分类目的地推荐
    print("\n热门目的地分类：")
    for 分类 in 地区分类:
        print(f"- {分类}：{', '.join(地区分类[分类])}")

    # 获取有效输入
    while True:
        目的地 = input("\n如果可以选择世界上任何一个地方，您最想去哪里？").strip()
        if 目的地:
            break
        print("⚠️ 请输入有效目的地！")

    # 存储结果
    调查结果[姓名] = 目的地

    # 继续调查
    继续 = input("\n是否让其他人继续参与调查？(y/n) ").lower()
    if 继续 != 'y':
        break

# 可视化结果报告
print("\n=== 调查结果分析 ===")
print(f"\n共收集到{len(调查结果)}份有效数据：")

for 序号, (姓名, 目的地) in enumerate(调查结果.items(), 1):
    print(f"{序号}. {姓名} 向往的目的地：{目的地}")

# 简单统计分析
热门目的地 = max(set(调查结果.values()), key=list(调查结果.values()).count)
print(f"\n★ 最受欢迎目的地：{热门目的地}")

print("\n感谢参与本次旅行调查！")

name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
