def clean_price(price_str: str) -> float:
    price_str = price_str.replace("Â", "")  # защита от кодировки
    price_str = price_str.replace("£", "")
    return float(price_str)


def rating_to_int(rating_str: str) -> int:
    mapping = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return mapping.get(rating_str, 0)
