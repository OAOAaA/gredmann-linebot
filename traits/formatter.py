def format_pairing_output(name_a, birth_a, traits_a, name_b, birth_b, traits_b, match_result, relation):
    return f"""🔮 命理配對分析（{relation}）

🎂 A：{birth_a} → 本性：{traits_a['numerology']['core']}｜星座：{traits_a['zodiac']}｜主牌：{traits_a['tarot']}｜五行：{traits_a['wuxing']}
🎂 B：{birth_b} → 本性：{traits_b['numerology']['core']}｜星座：{traits_b['zodiac']}｜主牌：{traits_b['tarot']}｜五行：{traits_b['wuxing']}

🧠 能量互補：{match_result['tarot_result']['interaction']}（{traits_a['tarot']} × {traits_b['tarot']}）
📊 五維能量距離：{match_result['energy_gap']}（本性差值為 {abs(traits_a['numerology']['core'] - traits_b['numerology']['core'])}）
🔥 五行相處：{traits_a['wuxing']} × {traits_b['wuxing']} → {match_result['wuxing_result']['relation']}

🗣 相處建議：{match_result['suggestion']}

📈 配對指數：{match_result['final_score']} / 100
"""
