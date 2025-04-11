
def format_pairing_output(result: dict, relation: str) -> str:
    zodiac = result.get("zodiac_result", {})
    tarot = result.get("tarot_result", {})
    wuxing = result.get("wuxing_result", {})

    return f"""
🔮 命理配對分析（{relation}）

📈 配對綜合分數：{result.get('final_score', '?')} / 100
🧠 本性差距：{result.get('energy_gap', '?')}

🌟 星座互動：{zodiac.get('type', '❓')}（{zodiac.get('detail', '無資料')}）→ 分數：{zodiac.get('compatibility_score', '?')}
🃏 主牌互動：{tarot.get('type', '❓')}（{tarot.get('detail', '無資料')}）→ 分數：{tarot.get('compatibility_score', '?')}
🔥 五行關係：{wuxing.get('interaction', '❓')}（{wuxing.get('detail', '無資料')}）→ 分數：{wuxing.get('score', '?')}

🗣 建議語錄：
{result.get('suggestion', '（尚無建議）')}
    """.strip()
