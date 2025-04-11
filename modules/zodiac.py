def get_zodiac(month: int, day: int) -> str:
    zodiacs = [
        (120, "摩羯"), (219, "水瓶"), (321, "雙魚"), (420, "牡羊"),
        (521, "金牛"), (621, "雙子"), (722, "巨蟹"), (823, "獅子"),
        (923, "處女"), (1023, "天秤"), (1122, "天蠍"), (1222, "射手"), (1231, "摩羯")
    ]
    value = month * 100 + day
    for zodiac_day, zodiac_name in zodiacs:
        if value <= zodiac_day:
            return zodiac_name
    return "摩羯"

def compare_zodiacs(z1: str, z2: str) -> dict:
    compatible = {
        ("天蠍", "雙魚"), ("處女", "金牛"), ("射手", "牡羊"),
        ("摩羯", "處女"), ("水瓶", "雙子"), ("巨蟹", "天蠍"),
        ("獅子", "射手"), ("雙魚", "巨蟹"), ("雙子", "天秤")
    }
    score = 90 if (z1, z2) in compatible or (z2, z1) in compatible else 65
    return {"compatible": (z1, z2) in compatible, "compatibility_score": score}
