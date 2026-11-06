# Python Junior Developer: 30-Day Fast-Track Roadmap

**Goal:** Become confident enough to contribute to a real Python backend project and apply for junior developer roles.
**Daily commitment:** 2-3 hours (30% learning, 70% coding).
**Status key:** `[ ]` not started · `[~]` in progress · `[x]` done

---

## How we work through each stage

1. **Concept:** I explain the idea briefly, with a small example.
2. **Explore:** You work it out yourself (docs, experiments, your own code). Attempt before asking AI to solve it.
3. **Outcome:** You paste your code, terminal output, or notes.
4. **Review:** I check correctness, style and tests, and tell you what to fix.
5. **Log:** I format your outcome into the stage's "Outcome log" below and tick the box. Then we move on.

Every stage ends with a **checkpoint**: you can explain it and do it without copying a tutorial.

---

## Progress overview

| Phase | Days | Focus | Status |
| --- | --- | --- | --- |
| 1 | 1-5 | Refresh Python | `[~]` (Days 1, 3, 5 done; Day 2 and Day 4 polish left) |
| 2 | 6-9 | Maintainable Python | `[ ]` |
| 3 | 10-15 | Databases and APIs | `[ ]` |
| 4 | 16-20 | Project 1: Task Management API | `[ ]` |
| 5 | 21-25 | Project 2: School Management API | `[ ]` |
| 6 | 26-30 | Project 3: Production-ready API | `[ ]` |

---

## Phase 1: Refresh Your Python (Days 1-5)

**Checkpoint:** You can write small Python programs without following a tutorial line by line.

| Day | Topic | Practical exercise | Status |
| --- | --- | --- | --- |
| 1 | Variables, data types, operators, strings | Diagnostic: student grading CLI | `[x]` |
| 2 | Lists, tuples, sets, dictionaries | Student records manager | `[ ]` |
| 3 | Conditions, loops, comprehensions | Student grading system | `[x]` (covered in Day 1 work) |
| 4 | Functions, arguments, scope, type hints | Refactor grading into reusable functions | `[~]` (functions and hints done; extend with persistence) |
| 5 | Exceptions, files, modules, imports | Save and retrieve student records from a file (JSON) | `[x]` |

### Outcome log

**Day 1: Diagnostic (student-grading-cli)** · Repo: `github.com/Emmalywebcreator/student-grading-cli`
- Built: CLI that collects a name and three scores, validates them, computes total/average, decides pass/fail (50+ in every subject).
- Bugs found and fixed: missing `else` (every student failed); missing `continue` after range check (invalid score accepted).
- Added: `get_name()` with `.strip()` and re-prompt; `has_passed` via `all()`; `PASS_MARK` constant; type hints.
- Tests: 17 `unittest` tests, including pass-mark boundaries (50 passes, 49 fails), validation, and total/average. Mutation check confirmed the tests catch broken arithmetic.
- Tooling: `ruff check`, `ruff format`, `.gitignore`, `__pycache__` untracked.
- Git: feature branch, 4 focused commits, PR merged into `main`.
- Lessons: a failing test is doing its job; read the actual output before changing code; `continue` after an error message is what forces re-entry.

**Day 5: File handling and JSON (feature/save-results)** · *Done*
- Built `storage.py`: `load_results(path)` returns `[]` when the file is missing; `save_result(name, total, path)` loads the list, appends one record, and writes the whole list back with mode `"w"`.
- Added `CorruptResultsError`: invalid JSON in the file is reported clearly instead of crashing with a raw `JSONDecodeError`, and `save_result` refuses to overwrite a corrupt file.
- Tests (22 in total, all passing): missing file, valid file, save into a missing file, save twice keeps the first record, saving does not overwrite a corrupt file. All use `tempfile.TemporaryDirectory()` so real data is never touched. Tests now live in `tests/` and run with `python3 -m unittest discover -s tests -v` from the project root.
- Thinking question: chose try-and-catch over check-first because the file can change between the check and the open (race condition), and it needs less code. Catch only the specific error you can handle (`FileNotFoundError`); let everything else fail loudly.
- Proof the tests protect the code: with `"a"` instead of `"w"`, the "save twice" test failed with `JSONDecodeError: Extra data`, while the single-save test still passed.
- Lessons: `open("path")` (quotes) opens a file literally named path, and `except FileNotFoundError: return []` hid that bug until a test checked real data; a `SyntaxError` in a test file makes the whole file vanish from the test count; `[...][...]` is indexing, not a list of two items; `json.dumps` (to string) vs `json.dump` (to file); run commands from the project root.
- Still to do: add a direct `load_results` test for the corrupt file (`assertRaises(CorruptResultsError)`), run `ruff check --fix . && ruff format . && ruff check .`, and commit and open the PR.

---

## Phase 2: Write Maintainable Python (Days 6-9)

**Checkpoint:** You can structure a small project, debug it, and manage it with Git.

| Day | Topic | Practical exercise | Status |
| --- | --- | --- | --- |
| 6 | Classes, objects, inheritance, encapsulation | Model students, teachers, courses | `[~]` (Student class done and wired into the CLI; teachers, courses, inheritance next) |
| 7 | Iteration, generators, decorators, built-ins | Practical data-processing problems | `[ ]` |
| 8 | Virtual environments, packages, debugging | Set up a clean Python project | `[ ]` (`.venv` already in use) |
| 9 | Git, GitHub, clean code, refactoring | Organise and version-control your project | `[ ]` (PR workflow already practised) |

### Outcome log

**Day 6: Classes and pytest (feature/student-class)** · *Student class built and wired into the CLI; teachers/courses/inheritance still to do*
- Switched to **pytest** for new tests (`pytest.ini` with `pythonpath = .` and `testpaths = tests`). Old `unittest` tests run unchanged under it.
- Built `models.py` test-first, one method per loop (red, then green): `Student(name, scores)` with `total()`, `average()`, `has_passed(pass_mark=50)` and `to_dict()`.
- Concepts: `__init__` and `self`, attributes vs methods, default parameters, `all(score >= pass_mark for score in self.scores.values())`, `pytest.approx` for floats, `@pytest.fixture` replacing `setUp`, `@pytest.mark.parametrize` for the 50 / 49 / high-average-one-fail boundary rows, `pytest.raises`.
- Edge case decisions: `average()` on empty scores raises `ValueError` (no scores means no average; returning `0.0` would hide the problem); `has_passed()` is `False` for empty scores, because `all()` of an empty collection is `True`.
- Mutation checks: changing `>=` to `>` failed the exactly-50 row; wrong dict key and bracket mistakes were caught immediately.
- Wiring (feature/wire-student): refactored `main()` to build a `Student` and use `total()`, `average()` and `has_passed()` (a refactor is verified by unchanged tests); moved the pass mark into `models.py`; retired the old standalone `has_passed` and folded its cases into the parametrized rows; connected `save_result(**student.to_dict())` (`**` unpacks a dict into keyword arguments).
- Protecting real data: tests that called `main()` wrote to the real `results.json` and hit `CorruptResultsError` on an empty file. Fixed with `tests/conftest.py`: an `autouse` fixture using `monkeypatch.setattr("main.save_result", ...)` (patch the name where it is used). Added `tests/test_cli_save.py`, which records the call and asserts `[{"name": "Talia", "total": 266}]`; mutation check (call commented out) failed with `assert [] == [...]`, then restored.
- Final state: 28 tests passing, real `results.json` untouched by the test run.
- Lessons: bracket type is meaning (`()` call, `[]` list/index, `{}` dict/set); `assert obj.method` without `()` can never fail and `obj.method` without `()` raises nothing; pytest shows `<Student object ...>.method` when you accidentally pass a bound method instead of its result; a test is only trustworthy after you have watched it fail for the right reason; read the `>` line and `E` lines first in a failure.
- More lessons: code at the top level of a module runs on import (a `NameError` there broke every test file that imported `main`); a collection error or a sudden drop in the test count means a file failed to import; when code moves, its tests move with it; unused imports get removed by `ruff --fix`, which can break a fixture that patches them.
- Open question to decide: is a 0-byte `results.json` corrupt, or just "no results yet"?
- Still to do: ruff pass, commit in pieces, open the PR for feature/wire-student.

---

## Phase 3: Databases and APIs (Days 10-15)

**Checkpoint:** You can design a small relational schema and expose it through a Flask API.

| Day | Topic | Practical exercise | Status |
| --- | --- | --- | --- |
| 10 | SQL fundamentals | Create and query a PostgreSQL database | `[ ]` |
| 11 | Relationships, joins, constraints, indexes | Model students, classes, results | `[ ]` |
| 12 | Python database access and SQLAlchemy | Connect Python to PostgreSQL | `[ ]` |
| 13 | HTTP, JSON, REST, status codes | Consume an external API | `[ ]` |
| 14 | Flask fundamentals and routing | First API endpoints | `[ ]` |
| 15 | Request validation and error handling | Reliable API responses | `[ ]` |

**Outcome log:** _(empty)_

---

## Phase 4: Project 1, Task Management API (Days 16-20)

**Features:** user registration and login · task CRUD · PostgreSQL · user-specific access control · input validation · consistent error responses · automated tests · API documentation.
**Deliverable:** A working REST API you can demonstrate to an interviewer.

| Step | Status |
| --- | --- |
| Project structure (routes / business logic / database / config) | `[ ]` |
| Auth: register and login | `[ ]` |
| Task CRUD with ownership checks | `[ ]` |
| Validation and error format | `[ ]` |
| Tests and API docs | `[ ]` |

**Outcome log:** _(empty)_

---

## Phase 5: Project 2, School Management API (Days 21-25)

**Features:** students and teachers · classes and subjects · enrollment · exam results · search and pagination · role-based permissions · database migrations · integration tests.

| Step | Status |
| --- | --- |
| Schema and migrations | `[ ]` |
| Students, teachers, classes endpoints | `[ ]` |
| Enrollment and results | `[ ]` |
| Roles and permissions | `[ ]` |
| Search, pagination, integration tests | `[ ]` |

**Outcome log:** _(empty)_

---

## Phase 6: Project 3, Production-Ready API (Days 26-30)

Take one project and add: Docker · GitHub Actions · automated testing · environment configuration · logging and health checks · migration procedures · deployment · a professional README. Finish with interview practice and a PR-style code review.

| Step | Status |
| --- | --- |
| Docker | `[ ]` |
| CI with GitHub Actions | `[ ]` |
| Config, logging, health checks | `[ ]` |
| Deployment | `[ ]` |
| README and interview practice | `[ ]` |

**Outcome log:** _(empty)_

---

## Must-know areas checklist (from the roadmap)

- [~] 1. Python fundamentals (files, JSON, exceptions covered)
- [~] 2. Git and GitHub (branches, PRs, `.gitignore` done; merge conflicts, stash still to practise)
- [ ] 3. SQL and database fundamentals
- [ ] 4. APIs and HTTP
- [ ] 5. One backend framework (Flask)
- [~] 6. Testing and debugging (unittest and pytest, mocking, boundaries, temp files, fixtures, parametrize, red-then-green, mutation checks)
- [~] 7. Clean code principles (ruff, type hints, naming)
- [ ] 8. Linux, terminal, environment management (venv in use)
- [ ] 9. Docker and deployment basics
- [ ] 10. Interview preparation

## Weakness tracker

| Concept | What went wrong | Revisit by |
| --- | --- | --- |
| `continue` vs fall-through in loops | Removed a needed `continue`; invalid score accepted | Day 6 |
| Tracking generated files in Git | `__pycache__` was committed | Fixed |
| Forgetting `()` when calling a method (twice in Day 6) | Tests passed or failed for the wrong reason (`assert obj.method`, `.average` in `pytest.raises`) | Check every `assert` with `grep -n assert tests/*.py` |
| Top-level code in a module that needs runtime values (`student_name`) | `NameError` on import broke test collection | Keep only `def`, `class`, imports and constants at module level |
| Typos in names and strings (`"path"` vs `path`, `encodinging`, `fisrt`) | Caused silent wrong behaviour and test errors | Run `ruff check .` after every edit |
| Writing a list of dicts in Python | `[...][...]` and merged dicts | Day 6 |
| Shell commands | `ruff check . and ruff format .`; running tests from inside `tests/` | Day 8 |

_Honest note: thirty days is an intensive preparation target, not a guarantee of employment readiness. If a concept needs more practice, we repeat it instead of abandoning the plan._
