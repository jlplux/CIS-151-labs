# test_practiceproblem1.py
import unittest
from practiceproblem1 import count_consonants, sum_positive, reverse_no_vowels, letter_frequency, filter_odd

class TestPracticeProblem1(unittest.TestCase):

    # -------------------------------
    # Test Problem 1 – Count Consonants
    # -------------------------------
    def test_count_consonants(self):
        self.assertEqual(count_consonants("hello"), 3)
        self.assertEqual(count_consonants("AEIOU"), 0)
        self.assertEqual(count_consonants("Python"), 5)

    # -------------------------------
    # Test Problem 2 – Sum Positive Integers
    # -------------------------------
    def test_sum_positive(self):
        self.assertEqual(sum_positive([1, -2, 3, 0]), 4)
        self.assertEqual(sum_positive([-1, -5, -10]), 0)
        self.assertEqual(sum_positive([]), 0)

    # -------------------------------
    # Test Problem 3 – Reverse String Without Vowels
    # -------------------------------
    def test_reverse_no_vowels(self):
        self.assertEqual(reverse_no_vowels("hello"), "llh")
        self.assertEqual(reverse_no_vowels("AEIOU"), "")
        self.assertEqual(reverse_no_vowels("Python"), "nhtyP")

    # -------------------------------
    # Test Problem 4 – Letter Frequency
    # -------------------------------
    def test_letter_frequency(self):
        self.assertEqual(letter_frequency("hello"), {'h':1,'e':1,'l':2,'o':1})
        self.assertEqual(letter_frequency("aaa"), {'a':3})
        self.assertEqual(letter_frequency(""), {})

    # -------------------------------
    # Test Problem 5 – Filter Odd Numbers
    # -------------------------------
    def test_filter_odd(self):
        self.assertEqual(filter_odd([1, 2, 3, 4]), [1, 3])
        self.assertEqual(filter_odd([2, 4, 6]), [])
        self.assertEqual(filter_odd([]), [])

if __name__ == "__main__":
    unittest.main()
