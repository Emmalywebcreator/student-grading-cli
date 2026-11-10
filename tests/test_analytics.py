import pytest

from analytics import above_average, class_average, ranking, top_scorer

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


def test_tie_returns_first_listed():
    records = [
        {"name": "John", "total": 180},
        {"name": "Stephen", "total": 300},
        {"name": "Mathew", "total": 300},
    ]
    assert (top_scorer(records)) == {"name": "Stephen", "total": 300}


def test_top_scorer_of_empty_list():
    assert top_scorer([]) is None


def test_class_average():
    assert class_average(RECORDS) == pytest.approx(232.0)


def test_class_average_of_empty_list_returns_none():
    assert class_average([]) is None


def test_above_average_returns_records_over_the_average():
    assert above_average(RECORDS) == [
        {"name": "Talia", "total": 266},
        {"name": "Mathew", "total": 250},
        # {"name": "John", "total": 180}
    ]


def test_above_average_of_empty_list_returns_empty_list():
    assert above_average([]) == []


def test_exact_average_is_not_above_average():
    records = [
        {"name": "A", "total": 100},
        {"name": "B", "total": 200},
        {"name": "C", "total": 150},
    ]
    assert above_average(records) == [{"name": "B", "total": 200}]


def test_ranking_orders_by_total_highest_first():
    assert ranking(RECORDS) == [
        (1, {"name": "Talia", "total": 266}),
        (2, {"name": "Mathew", "total": 250}),
        (3, {"name": "John", "total": 180}),
    ]


def test_ranking_does_not_change_the_input():
    original = [dict(r) for r in RECORDS]
    ranking(RECORDS)
    assert RECORDS == original


def test_ranking_tie_keeps_listed_order():
    records = [
        {"name": "John", "total": 200},
        {"name": "Talia", "total": 200},
    ]
    assert ranking(records) == [
        (1, {"name": "John", "total": 200}),
        (2, {"name": "Talia", "total": 200}),
    ]


def test_ranking_of_empty_list():
    assert ranking([]) == []
