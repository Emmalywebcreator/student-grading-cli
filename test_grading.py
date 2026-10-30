import unittest

from main import has_passed


class TestHasPassed(unittest.TestCase):
    def test_all_scores_above_pass_mark(self):
        self.assertTrue(has_passed(90, 69, 70))

    def test_all_scores_below_pass_mark(self):
        self.assertFalse(has_passed(40, 34, 45))

    def test_one_subject_below_pass_mark(self):
        self.assertFalse(has_passed(40, 80, 90))

    def test_all_subject_with_same_score(self):
        self.assertTrue(has_passed(50, 50, 50))

    def test_one_subject_at_below_boundary(self):
        self.assertFalse(has_passed(49, 50, 50))
