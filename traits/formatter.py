def format_pairing_output(result: dict, relation: str) -> str:
    zodiac = result["zodiac_result"]
    tarot = result["tarot_result"]
    wuxing = result["wuxing_result"]

    return f"""
🔮 命理配對分析（{relation}）

📈 配對綜合分數：{result['final_score']} / 100
🧠 本性差距：{result['energy_gap']}

🌟 星座互動：{zodiac['type']}（{zodiac['detail']}）→ 分數：{zodiac['compatibility_score']}
🃏 主牌互動：{tarot['type']}（{tarot['detail']}）→ 分數：{tarot['compatibility_score']}
🔥 五行關係：{wuxing['interaction']}（{wuxing['detail']}）→ 分數：{wuxing['score']}

🗣 建議語錄：
{result['suggestion']}
    """.strip()
