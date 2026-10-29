import unittest
from main import has_passed


class TestHasPassed(unittest.TestCase):

    def test_all_scores_above_pass_mark(self):
        self.assertTrue(has_passed(90, 69, 70))
     #   self.assertTrue(has_passed, 90)
    #    self.assertTrue(has_passed, 80)

    def test_all_scores_below_pass_mark(self):
        self.assertFalse(has_passed(40, 34, 45))
     #   self.assertTrue(has_passed, 34)
      #  self.assertTrue(has_passed, 49)
       # self.assertTrue(has_passed, 45)

    def test_one_subject_below_pass_mark(self):
        self.assertFalse(has_passed(40, 80, 90))
