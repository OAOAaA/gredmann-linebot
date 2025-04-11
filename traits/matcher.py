from modules.zodiac import compare_zodiacs
from modules.tarot import compare_tarot_cards
from modules.wuxing import compare_elements
from modules.suggestion import get_pairing_suggestion

def match_pairing(a_traits: dict, b_traits: dict, relation: str) -> dict:
    zodiac_result = compare_zodiacs(a_traits["zodiac"], b_traits["zodiac"])
    tarot_result = compare_tarot_cards(a_traits["tarot"], b_traits["tarot"])
    wuxing_result = compare_elements(a_traits["wuxing"], b_traits["wuxing"])

    # 本性能量差距
    num_diff = abs(a_traits["numerology"]["core"] - b_traits["numerology"]["core"])
    num_score = 20 if num_diff == 0 else 15 if num_diff == 1 else 10 if num_diff <= 3 else 5

    # 紫微性格交集
    trait_overlap = len(set(a_traits["ziwei"]["traits"]) & set(b_traits["ziwei"]["traits"]))
    ziwei_score = 10 if trait_overlap >= 2 else 5 if trait_overlap == 1 else 3

    # 卦象互補（略加分）
    yijing_score = 5 if a_traits["yijing"]["hexagram_index"] != b_traits["yijing"]["hexagram_index"] else 3

    # 加權總分
    final_score = round((
        zodiac_result["compatibility_score"] * 0.2 +
        tarot_result["compatibility_score"] * 0.25 +
        wuxing_result["score"] * 0.25 +
        num_score * 0.15 +
        ziwei_score * 0.1 +
        yijing_score * 0.05
    ))

    suggestion = get_pairing_suggestion(
        relation, final_score,
        a_traits["ziwei"]["traits"], b_traits["ziwei"]["traits"]
    )

    return {
        "zodiac_result": zodiac_result,
        "tarot_result": tarot_result,
        "wuxing_result": wuxing_result,
        "energy_gap": f"本性差值為 {num_diff}",
        "final_score": final_score,
        "suggestion": suggestion
    }
