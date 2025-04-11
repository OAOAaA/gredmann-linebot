def get_ziwei_ming_gong(year: int, month: int, day: int) -> dict:
    stars = ["紫微", "天機", "太陽", "武曲", "天同", "廉貞", "天府", "太陰", "貪狼", "巨門", "天相", "天梁", "七殺", "破軍"]
    index = (year + month + day) % len(stars)
    return {
        "ming_gong": f"{['子宮','丑宮','寅宮','卯宮','辰宮','巳宮','午宮','未宮','申宮','酉宮','戌宮','亥宮'][index % 12]}",
        "main_star": stars[index],
        "traits": ["變革", "獨立", "不服輸"] if stars[index] == "破軍" else ["沉穩", "謹慎", "包容"]
    }
