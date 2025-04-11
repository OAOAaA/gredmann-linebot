def calculate_numbers(year: int, month: int, day: int) -> dict:
    core = sum(int(c) for c in str(year)[-2:])
    base = int(f"{year}{month:02}{day:02}")
    total = sum(int(d) for d in str(base))
    outer = sum(int(d) for d in str(total))
    if outer > 22:
        outer -= 22
    inner = outer if outer < 22 else sum(map(int, str(outer)))
    return {
        "core": core,
        "outer": outer,
        "inner": inner
    }
