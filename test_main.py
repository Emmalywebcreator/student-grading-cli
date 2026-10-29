#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from main import get_score


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
