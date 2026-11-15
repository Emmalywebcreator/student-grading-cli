import json
from pathlib import Path


class CorruptResultsError(Exception):
    "Raised when the results file exists but is not valid JSON."


def load_results(path: str | Path = "results.json") -> list[dict]:
    """Return the results, or an empty list if there is no file"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return []
    except json.JSONDecodeError as error:
        raise CorruptResultsError(f"{path} is corrupted; fix or delete it") from error


def save_result(name: str, total: int, path: str | Path = "results.json") -> None:
    """Append one student's result to the json file"""
    records = load_results(path)

    new_record = {"name": name, "total": total}

    records.append(new_record)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


if __name__ == "__main__":
    save_result("Talia", 266, "scratch.json")
    save_result("John", 180, "scratch.json")
    save_result("Mathew", 250, "results.json")
    print(load_results("scratch.json"))
