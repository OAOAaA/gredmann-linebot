def get_tarot_card(month: int, day: int) -> str:
    cards = ["愚人", "魔術師", "女祭司", "皇后", "皇帝", "教皇", "戀人", "戰車", "力量", "隱者",
             "命運之輪", "正義", "吊人", "死神", "節制", "惡魔", "高塔", "星星", "月亮", "太陽", "審判", "世界"]
    index = (month + day) % len(cards)
    return cards[index]

def compare_tarot_cards(card1: str, card2: str) -> dict:
    interaction = "轉化型關係" if (card1, card2) != (card2, card1) else "鏡像效應"
    score = 85 if interaction == "轉化型關係" else 70
    return {"interaction": interaction, "compatibility_score": score}
