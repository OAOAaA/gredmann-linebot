from modules.zodiac import compare_zodiacs
from modules.tarot import compare_tarot_cards
from modules.wuxing import compare_elements
from modules.suggestion import get_pairing_suggestion

def match_pairing(a_traits: dict, b_traits: dict, relation: str) -> dict:
    zodiac_result = compare_zodiacs(a_traits["zodiac"], b_traits["zodiac"])
    tarot_result = compare_tarot_cards(a_traits["tarot"], b_traits["tarot"])
    wuxing_result = compare_elements(a_traits["wuxing"], b_traits["wuxing"])
    diff = abs(a_traits["numerology"]["core"] - b_traits["numerology"]["core"])
    energy_gap = "相近" if diff == 0 else "適中" if diff <= 3 else "差異較大"
    avg_score = round((zodiac_result["compatibility_score"] +
                       tarot_result["compatibility_score"] +
                       wuxing_result["score"]) / 3)
    suggestion = get_pairing_suggestion(relation, avg_score,
                                        a_traits["ziwei"]["traits"],
                                        b_traits["ziwei"]["traits"])
    return {
        "zodiac_result": zodiac_result,
        "tarot_result": tarot_result,
        "wuxing_result": wuxing_result,
        "energy_gap": energy_gap,
        "final_score": avg_score,
        "suggestion": suggestion
    }
