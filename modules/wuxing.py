def get_element_from_year(year: int) -> str:
    elements = ["金", "水", "木", "火", "土"]
    return elements[year % 5]

def compare_elements(e1: str, e2: str) -> dict:
    relations = {
        ("水", "木"): "相生", ("木", "火"): "相生", ("火", "土"): "相生", ("土", "金"): "相生", ("金", "水"): "相生",
        ("木", "水"): "相剋", ("火", "金"): "相剋", ("土", "水"): "相剋", ("金", "火"): "相剋", ("水", "土"): "相剋"
    }
    key = (e1, e2)
    relation = relations.get(key, "中性")
    score = 90 if relation == "相生" else 60 if relation == "相剋" else 75
    return {"relation": relation, "score": score}
