import unittest
import lab5


class MyTestCase(unittest.TestCase):
    def test_right_justify(self):
        result = lab5.right_justify("asdfa")
        self.assertEqual("---", result)
        result = lab5.right_justify("asd")
        self.assertEqual("asd", result)
        result = lab5.right_justify("qwe")
        self.assertEqual("qwe", result)
        result = lab5.right_justify("po")
        self.assertEqual(" po", result)
        result = lab5.right_justify("p")
        self.assertEqual("  p", result)
        result = lab5.right_justify("")
        self.assertEqual("   ", result)

    def test_is_vowel(self):
        self.assertTrue(lab5.is_vowel("a"))
        self.assertTrue(lab5.is_vowel("e"))
        self.assertTrue(lab5.is_vowel("i"))
        self.assertTrue(lab5.is_vowel("o"))
        self.assertTrue(lab5.is_vowel("u"))
        self.assertFalse(lab5.is_vowel("ua"))
        self.assertFalse(lab5.is_vowel("we"))
        self.assertFalse(lab5.is_vowel("w"))
        self.assertFalse(lab5.is_vowel("d"))

    def test_fizzbuzz(self):
        result = lab5.fizzbuzz(9)
        self.assertEqual("fizz", result)
        result = lab5.fizzbuzz(10)
        self.assertEqual("buzz", result)
        result = lab5.fizzbuzz(15)
        self.assertEqual("fizzbuzz", result)
        result = lab5.fizzbuzz(29)
        self.assertEqual("", result)


if __name__ == '__main__':
    unittest.main()