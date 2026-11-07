def top_scorer(records: list[dict]) -> dict | None:
    """Return the record with the highest total"""
    return max(records, key=lambda r: r["total"])
