import main


def test_main_saves_the_result(monkeypatch):
    calls = []
    monkeypatch.setattr(main, "save_result", lambda **kwargs: calls.append(kwargs))
    answers = iter(["Talia", "87", "90", "89"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))

    main.main()

    assert calls == [{"name": "Talia", "total": 266}]
