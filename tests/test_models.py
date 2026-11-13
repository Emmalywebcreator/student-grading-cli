import pytest

from models import Student


@pytest.fixture
def student() -> Student:
    return Student("Talia", {"Maths": 87, "English": 90, "CSC": 89})


def test_total(student):
    assert student.total() == 266


def test_average(student):
    assert student.average() == pytest.approx(88.67, abs=0.01)


@pytest.mark.parametrize(
    ("scores", "expected"),
    [
        ({"Maths": 90, "English": 69, "CSC": 70}, True),  # all comfortably above
        ({"Maths": 40, "English": 34, "CSC": 45}, False),  # all below
        ({"Maths": 50, "English": 50, "CSC": 50}, True),
        ({"Maths": 49, "English": 50, "CSC": 50}, False),
        ({"Maths": 94, "English": 92, "CSC": 45}, False),
    ],
)
def test_has_passed_boundaries(scores, expected):
    student = Student("Talia", scores)
    assert student.has_passed() == expected


def test_to_dict_returns_name_and_total(student):
    assert student.to_dict() == {"name": "Talia", "total": 266}


def test_average_with_no_score_raises():
    with pytest.raises(ValueError):
        Student("Talia", {}).average()


def test_has_not_passed_with_no_scores():
    assert Student("Talia", {}).has_passed() is False
