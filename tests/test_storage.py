import json
import tempfile
import unittest
from pathlib import Path

from storage import CorruptResultsError, load_results, save_result


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


class TestSaveResult(unittest.TestCase):
    def test_creates_file_with_one_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.json"
            save_result("Talia", 266, path)
            self.assertEqual(load_results(path), [{"name": "Talia", "total": 266}])

    def test_second_save_keeps_first_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.json"
            save_result("Talia", 266, path)
            save_result("John", 180, path)
            self.assertEqual(
                load_results(path),
                [{"name": "Talia", "total": 266}, {"name": "John", "total": 180}],
            )

    def test_save_does_not_overwrite_corrupt_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.json"
            path.write_text("{not valid json", encoding="utf-8")
            with self.assertRaises(CorruptResultsError):
                save_result("Talia", 266, path)
            self.assertEqual(path.read_text(encoding="utf-8"), "{not valid json")
