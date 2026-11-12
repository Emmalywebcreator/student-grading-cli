import pytest

from utils import timed


def test_timed_returns_the_original_result():
    @timed
    def add(a, b):
        return a + b

    assert add(2, 3) == 5


def test_timed_passes_keyword_arguements():
    @timed
    def greet(name, punctuations="!"):
        return f"Hi {name}{punctuations}"

    assert greet("Talia", punctuations="?") == "Hi Talia?"


def test_timed_keeps_the_function_name():
    @timed
    def add(a, b):
        return a + b

    assert add.__name__ == "add"


def test_timed_prints_name_and_duration(capsys):
    @timed
    def add(a, b):
        return a + b

    add(1, 2)
    output = capsys.readouterr().out
    assert "add" in output
    assert "took" in output


def test_timed_lets_errors_through():
    @timed
    def fail():
        raise ZeroDivisionError

    with pytest.raises(ZeroDivisionError):
        fail()


def test_timed_prints_even_when_the_function_fails(capsys):
    @timed
    def fail():
        raise ZeroDivisionError

    with pytest.raises(ZeroDivisionError):
        fail()
    assert "fail took" in capsys.readouterr().out
