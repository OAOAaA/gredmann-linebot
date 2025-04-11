def parse_pairing_command(text):
    text = text.replace("配對：", "").strip()
    parts = text.split("，")
    if len(parts) != 2:
        raise ValueError("格式錯誤，請使用：配對：1990/01/01 與 1995/05/05，朋友")
    birthdays, relation = parts
    if "與" not in birthdays:
        raise ValueError("生日中請使用 '與' 連接")
    person1, person2 = birthdays.split("與")
    return person1.strip(), person2.strip(), relation.strip()
