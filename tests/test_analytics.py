import pytest

from analytics import above_average, class_average, ranking, top_scorer


@pytest.fixture
def records():
    return [
        {"name": "Talia", "total": 266},
        {"name": "John", "total": 180},
        {"name": "Mathew", "total": 250},
    ]


def test_top_scorer_returns_highest_total(records):
    assert top_scorer(records) == {"name": "Talia", "total": 266}


def test_top_scorer_when_top_is_not_first():
    records_data = [
        {"name": "John", "total": 180},
        {"name": "Mathew", "total": 290},
        {"name": "Talia", "total": 266},
    ]
    assert top_scorer(records_data) == {"name": "Mathew", "total": 290}


def test_tie_returns_first_listed():
    records_data = [
        {"name": "John", "total": 180},
        {"name": "Stephen", "total": 300},
        {"name": "Mathew", "total": 300},
    ]
    assert (top_scorer(records_data)) == {"name": "Stephen", "total": 300}


def test_top_scorer_of_empty_list():
    assert top_scorer([]) is None


def test_class_average(records):
    assert class_average(records) == pytest.approx(232.0)


def test_class_average_of_empty_list_returns_none():
    assert class_average([]) is None


def test_above_average_returns_records_over_the_average(records):
    assert above_average(records) == [
        {"name": "Talia", "total": 266},
        {"name": "Mathew", "total": 250},
    ]


def test_above_average_of_empty_list_returns_empty_list():
    assert above_average([]) == []


def test_exact_average_is_not_above_average():
    records_data = [
        {"name": "A", "total": 100},
        {"name": "B", "total": 200},
        {"name": "C", "total": 150},
    ]
    assert above_average(records_data) == [{"name": "B", "total": 200}]


def test_ranking_orders_by_total_highest_first(records):
    assert ranking(records) == [
        (1, {"name": "Talia", "total": 266}),
        (2, {"name": "Mathew", "total": 250}),
        (3, {"name": "John", "total": 180}),
    ]


def test_ranking_does_not_change_the_input(records):
    original = [dict(r) for r in records]
    ranking(records)
    assert records == original


def test_ranking_tie_keeps_listed_order():
    records_data = [
        {"name": "John", "total": 200},
        {"name": "Talia", "total": 200},
    ]
    assert ranking(records_data) == [
        (1, {"name": "John", "total": 200}),
        (2, {"name": "Talia", "total": 200}),
    ]


def test_ranking_of_empty_list():
    assert ranking([]) == []
