# test_practice_problems.py
import unittest
from practice_problems import count_vowels, sum_integers, remove_vowels, word_frequency, filter_even

class TestPracticeProblems(unittest.TestCase):

    # -------------------------------
    # Test Problem 1 – Count Vowels
    # -------------------------------
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("sky"), 0)
        self.assertEqual(count_vowels("AEIOU"), 5)

    # -------------------------------
    # Test Problem 2 – Sum of Integers
    # -------------------------------
    def test_sum_integers(self):
        self.assertEqual(sum_integers([1, 2, 3, 4]), 10)
        self.assertEqual(sum_integers([10, -5, 0]), 5)
        self.assertEqual(sum_integers([]), 0)

    # -------------------------------
    # Test Problem 3 – Remove Vowels
    # -------------------------------
    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("hello"), "hll")
        self.assertEqual(remove_vowels("AEIOU"), "")
        self.assertEqual(remove_vowels("python"), "pythn")

    # -------------------------------
    # Test Problem 4 – Word Frequency
    # -------------------------------
    def test_word_frequency(self):
        self.assertEqual(word_frequency(["cat", "dog", "cat"]), {"cat": 2, "dog": 1})
        self.assertEqual(word_frequency([]), {})
        self.assertEqual(word_frequency(["hello", "hello", "hello"]), {"hello": 3})

    # -------------------------------
    # Test Problem 5 – Filter Even Numbers
    # -------------------------------
    def test_filter_even(self):
        self.assertEqual(filter_even([1, 2, 3, 4]), [2, 4])
        self.assertEqual(filter_even([1, 3, 5]), [])
        self.assertEqual(filter_even([]), [])

if __name__ == "__main__":
    unittest.main()
