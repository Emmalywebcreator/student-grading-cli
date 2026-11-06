import pytest


@pytest.fixture(autouse=True)
def no_real_saves(monkeypatch):
    """Stop every test from writing to the real results file"""
    monkeypatch.setattr("main.save_result", lambda *args, **kwargs: None)
