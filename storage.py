import json
from pathlib import Path

def load_results(path: str | Path =  "results.json") -> list[dict]:
    '''Return the results, or an empty list if there is no file'''
    try:
        with open('path', "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return []

if __name__ == "__main__":
    print(load_results())
    print(load_results("nothing.json"))
