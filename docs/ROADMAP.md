# Python Junior Developer: 30-Day Fast-Track Roadmap

**Goal:** Become confident enough to contribute to a real Python backend project and apply for junior developer roles.
**Daily commitment:** 2-3 hours (30% learning, 70% coding).
**Status key:** `[ ]` not started · `[~]` in progress · `[x]` done

---

## How we work through each stage

1. **Concept:** I(Claude AI) explain the idea briefly, with a small example.
2. **Explore:** You work it out yourself (docs, experiments, your own code). Attempt before asking AI to solve it.
3. **Outcome:** You paste your code, terminal output, or notes.
4. **Review:** I check correctness, style and tests, and tell you what to fix.
5. **Log:** I format your outcome into the stage's "Outcome log" below and tick the box. Then we move on.

Every stage ends with a **checkpoint**: you can explain it and do it without copying a tutorial.

---

## Progress overview

| Phase | Days | Focus | Status |
| --- | --- | --- | --- |
| 1 | 1-5 | Refresh Python | `[~]` |
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
| 5 | Exceptions, files, modules, imports | Save and retrieve student records from a file (JSON) | `[~]` next up |

### Outcome log

**Day 1-4: Diagnostic (student-grading-cli)** · Repo: `github.com/Emmalywebcreator/student-grading-cli`
- Built: CLI that collects a name and three scores, validates them, computes total/average, decides pass/fail (50+ in every subject).
- Bugs found and fixed: missing `else` (every student failed); missing `continue` after range check (invalid score accepted).
- Added: `get_name()` with `.strip()` and re-prompt; `has_passed` via `all()`; `PASS_MARK` constant; type hints.
- Tests: 17 `unittest` tests, including pass-mark boundaries (50 passes, 49 fails), validation, and total/average. Mutation check confirmed the tests catch broken arithmetic.
- Tooling: `ruff check`, `ruff format`, `.gitignore`, `__pycache__` untracked.
- Git: feature branch, 4 focused commits, PR merged into `main`.
- Lessons: a failing test is doing its job; read the actual output before changing code; `continue` after an error message is what forces re-entry.

**Day 5: File handling and JSON (feature/save-results)** · *In progress*
- Task: `storage.py` with `load_results(path="results.json") -> list[dict]` (returns `[]` if missing), then `save_result(...)`, then handle corrupt JSON.
- Tests use `tempfile.TemporaryDirectory()`; add `results.json` to `.gitignore`.
- Outcome: _(paste here)_

---

## Phase 2: Write Maintainable Python (Days 6-9)

**Checkpoint:** You can structure a small project, debug it, and manage it with Git.

| Day | Topic | Practical exercise | Status |
| --- | --- | --- | --- |
| 6 | Classes, objects, inheritance, encapsulation | Model students, teachers, courses | `[ ]` |
| 7 | Iteration, generators, decorators, built-ins | Practical data-processing problems | `[ ]` |
| 8 | Virtual environments, packages, debugging | Set up a clean Python project | `[ ]` (`.venv` already in use) |
| 9 | Git, GitHub, clean code, refactoring | Organise and version-control your project | `[ ]` (PR workflow already practised) |

**Outcome log:** _(empty)_

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

- [~] 1. Python fundamentals
- [~] 2. Git and GitHub (branches, PRs, `.gitignore` done; merge conflicts, stash still to practise)
- [ ] 3. SQL and database fundamentals
- [ ] 4. APIs and HTTP
- [ ] 5. One backend framework (Flask)
- [~] 6. Testing and debugging (unittest, mocking, boundaries done; pytest still to learn)
- [~] 7. Clean code principles (ruff, type hints, naming)
- [ ] 8. Linux, terminal, environment management (venv in use)
- [ ] 9. Docker and deployment basics
- [ ] 10. Interview preparation

## Weakness tracker

| Concept | What went wrong | Revisit by |
| --- | --- | --- |
| `continue` vs fall-through in loops | Removed a needed `continue`; invalid score accepted | Day 6 |
| Tracking generated files in Git | `__pycache__` was committed | Fixed |

_Honest note: thirty days is an intensive preparation target, not a guarantee of employment readiness. If a concept needs more practice, we repeat it instead of abandoning the plan._