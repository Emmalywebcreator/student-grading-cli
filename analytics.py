def top_scorer(records: list[dict]) -> dict | None:
    """Return the record with the highest total"""
    return max(records, key=lambda r: r["total"], default=None)

def class_average(records: list[dict]) -> float | None:
    """Return the average total, or None if there are no records."""
    if not records:
        return None
    return sum(r["total"] for r in records) / len(records)
