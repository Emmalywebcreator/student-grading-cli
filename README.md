# Student Grading CLI

A beginner Python command-line application that collects a student's
scores in Mathematics, English, and Computer Science.

## Features

- Collects the student's name and subject scores.
- Validates scores between 0 and 100.
- Calculates the total and average score.
- Determines the overall result.
- Requires a score of at least 50 in every subject to pass.
- Saves each result to `results.json`. A corrupted results file is reported
  instead of being overwritten.

## Requirements

- Python 3.10 or newer (developed on Python 3.12)

## Setup

```bash
git clone https://github.com/Emmalywebcreator/student-grading-cli.git
cd student-grading-cli
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

To only run the app, `pip install -r requirements.txt` is enough. The app uses
only the Python standard library.

## Run the application

```bash
python3 main.py
```

## Run the tests and checks

```bash
pytest -q
ruff check .
ruff format --check .
```

## Project layout

- `main.py`: the command-line program.
- `models.py`: the `Student` class (total, average, pass/fail).
- `storage.py`: saving and loading results in `results.json`.
- `analytics.py`: functions that work on a list of saved results (top scorer,
  class average, ranking). Not used by the command-line program yet.
- `utils.py`: the `@timed` decorator.
- `tests/`: the test suite.
