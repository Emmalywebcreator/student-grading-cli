import json
import tempfile
import unittest
from pathlib import Path

from storage import load_results


class TestLoadResults(unittest.TestCase):
    def test_missing_file_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.json"
            self.assertEqual(load_results(path), [])

    def test_valid_file_is_loaded(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "result.json"
            data = [{"name": "Talia", "total": 266}]
            json_text = json.dumps(data)
            path.write_text(json_text, encoding="utf-8")
            self.assertEqual(load_results(path), data)
