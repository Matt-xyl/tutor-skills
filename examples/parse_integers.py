def parse_integers(text):
    if not text.strip():
        return []

    items = [item.strip() for item in text.split(",")]
    if any(item == "" for item in items):
        raise ValueError("Empty item in comma-separated input")

    return [int(item) for item in items]