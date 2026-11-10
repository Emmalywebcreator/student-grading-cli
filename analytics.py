def top_scorer(records: list[dict]) -> dict | None:
    """Return the record with the highest total"""
    return max(records, key=lambda r: r["total"], default=None)


def class_average(records: list[dict]) -> float | None:
    """Return the average total, or None if there are no records."""
    if not records:
        return None
    return sum(r["total"] for r in records) / len(records)


def above_average(records: list[dict]) -> list[dict]:
    """Return the records whose total is above the class average."""
    average = class_average(records)
    if average is None:
        return []
    return [r for r in records if r["total"] > average]


def ranking(records: list[dict]) -> list[tuple[int, dict]]:
    """Return (position, record) pairs, highest total first."""
    return list(
        enumerate(sorted(records, key=lambda r: r["total"], reverse=True), start=1)
    )
