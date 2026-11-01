#!/usr/bin/env python3

import unittest
from io import StringIO
from unittest.mock import patch

from main import get_name, get_score, main


class TestGetName(unittest.TestCase):
    @patch("builtins.input", return_value=" John Smith ")
    def test_strips_surrounding_whitespace(self, mock_input):
        self.assertEqual(get_name(), "John Smith")

    @patch("builtins.input", side_effect=["", " ", "Talia"])
    def test_rejects_empty_and_blank_names(self, mock_input):
        self.assertEqual(get_name(), "Talia")
        self.assertEqual(mock_input.call_count, 3)


class TestMainResult(unittest.TestCase):
    def test_passing_student_sees_pass_message(self):
        inputs = ["Talia", "87", "90", "89"]

        with (
            patch("builtins.input", side_effect=inputs),
            patch("sys.stdout", new_callable=StringIO) as output,
        ):
            main()

        self.assertIn(
            "Overall Result: Congratulations! You passed successfully.",
            output.getvalue(),
        )

    def test_failing_student_sees_fail_message(self):
        inputs = ["John", "90", "67", "45"]

        with (
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

    @patch("builtins.input", side_effect=["-1", "85"])
    def test_negative_input(self, mock_input):
        maths_result = get_score("Mathematics")
        self.assertEqual(maths_result, 85)

    @patch("builtins.input", side_effect=["101", "75"])
    def test_too_high_input(self, mock_input):
        maths_result = get_score("Mathematics")
        self.assertEqual(maths_result, 75)


class TestTotalAndAverage(unittest.TestCase):
    def test_summary_shows_correct_total_and_average(self):
        inputs = ["Talia", "87", "90", "89"]

        with (
            patch("builtins.input", side_effect=inputs),
            patch("sys.stdout", new_callable=StringIO) as output,
        ):
            main()

        self.assertIn("Total Score: 266", output.getvalue())
        self.assertIn("Average Score: 88.67", output.getvalue())
