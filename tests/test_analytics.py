import pytest

from analytics import top_scorer

RECORDS = [
    {"name": "Talia", "total": 266},
    {"name": "John", "total": 180},
    {"name": "Mathew", "total": 250},
]


def test_top_scorer_returns_highest_total():
    assert top_scorer(RECORDS) == {"name": "Talia", "total": 266}


def test_top_scorer_when_top_is_not_first():
    records = [
        {"name": "John", "total": 180},
        {"name": "Mathew", "total": 290},
        {"name": "Talia", "total": 266},
    ]
    assert top_scorer(records) == {"name": "Mathew", "total": 290}


def test_top_scorer_with_tie():
    records = [
        {"name": "John", "total": 180},
        {"name": "Stephen", "total": 300},
        {"name": "Mathew", "total": 300},
    ]
    assert (top_scorer(records)) == {"name": "Stephen", "total": 300}


def test_top_scorer_of_empty_list():
    # assert top_scorer([]) is None
    with pytest.raises(ValueError):
        top_scorer([])
