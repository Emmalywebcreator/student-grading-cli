class Student:
    """A student and their subject scores."""

    def __init__(self, name: str, scores: dict[str, int]) -> None:
        self.name = name
        self.scores = scores

    def total(self) -> int:
        return sum(self.scores.values())

    def average(self) -> float:
        if not self.scores:
            raise ValueError("User never enters any score")
        else:
            return self.total() / len(self.scores)

    def has_passed(self, pass_mark: int = 50) -> bool:
        if not self.scores:
            return False
        return all(score >= pass_mark for score in self.scores.values())

    def to_dict(self) -> dict[str, str | int]:
        return {"name": self.name, "total": self.total()}
