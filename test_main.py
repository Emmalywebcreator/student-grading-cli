#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from main import get_score, main
from io import StringIO

class TestMainResult(unittest.TestCase):

    def test_passing_student_sees_pass_message(self):
        inputs = ["Talia", "87", "90", "89"]

        with (
            patch("builtins.input", side_effect=inputs),
            patch("sys.stdout", new_callable=StringIO) as output,
        ):
            main()

        self.assertIn(
            "Overall Result: Congratulation! You passed successfully.",
            output.getvalue()
        )

    def test_failing_student_sees_fail_message(self):
        inputs = ["John", "90", "67", "45"]

        with(
            patch("builtins.input", side_effect=inputs),
            patch("sys.stdout", new_callable=StringIO) as output,
        ):
            main()
        self.assertIn(
            "Overall Result: Sorry you fail, didn't meet the requirement.",
            output.getvalue(),
        )


class TestGetScore(unittest.TestCase):
    @patch("builtins.input", return_value="0")
    def test_valid_score_0(self, mock_input):
        maths_result = get_score("Mathematics")
        self.assertEqual(maths_result, 0)

    @patch("builtins.input", return_value="100")
    def test_valid_score_100(self, mock_input):
        maths_result = get_score("Mathematics")
        self.assertEqual(maths_result, 100)

    @patch("builtins.input", return_value="75")
    def test_valid_score_75(self, mock_input):
        maths_result = get_score("Mathematics")
        self.assertEqual(maths_result, 75)

    @patch("builtins.input", return_value="80")
    def test_valid_score_80(self, mock_input):
        maths_result = get_score("Mathematics")
        self.assertEqual(maths_result, 80)

    @patch("builtins.input", side_effect=["hello", "70"])
    def test_non_numeric_input(self, mock_input):
        maths_result = get_score("Mathematics")
        self.assertEqual(maths_result, 70)
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input", side_effect=["-5", "85"])
    def test_negative_input(self, mock_input):
        maths_result = get_score("Mathematics")
        self.assertEqual(maths_result, 85)

    @patch("builtins.input", side_effect=["105", "75"])
    def test_too_high_input(self, mock_input):
        maths_result = get_score("Mathematics")
        self.assertEqual(maths_result, 75)
