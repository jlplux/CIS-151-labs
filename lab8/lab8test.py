import unittest
import lab8


class MyTestCase(unittest.TestCase):
    def test_magic_index(self):
        result = lab8.magic_index([1, 0, 3, 2])
        self.assertEqual(-1, result)
        result = lab8.magic_index([0, 4, 3, 2])
        self.assertEqual(0, result)
        result = lab8.magic_index([4, 1, 3, 2])
        self.assertEqual(1, result)
        result = lab8.magic_index([1, 0, 2, 4])
        self.assertEqual(2, result)
        result = lab8.magic_index([1, 0, 4, 3])
        self.assertEqual(3, result)

    def test_longer_than(self):
        test_data = ["a", "ab", "abc", "abcd"]
        result = lab8.longer_than(test_data, "two")
        self.assertEqual("abcd", result)
        result = lab8.longer_than(test_data, "three")
        self.assertEqual("", result)

    def test_num_longer_than(self):
        test_data = ["a", "ab", "abc", "abcd"]
        result = lab8.num_longer_than(test_data, "1")
        self.assertEqual(3, result)
        result = lab8.num_longer_than(test_data, "12")
        self.assertEqual(2, result)
        result = lab8.num_longer_than(test_data, "123")
        self.assertEqual(1, result)
        result = lab8.num_longer_than(test_data, "1234")
        self.assertEqual(0, result)

    def test_get_second_index(self):
        test_data = "one and two and one again and two"
        result = lab8.get_second_index(test_data, "one")
        self.assertEqual(16, result)
        result = lab8.get_second_index(test_data, "and")
        self.assertEqual(12, result)
        result = lab8.get_second_index(test_data, "nothere")
        self.assertEqual(-1, result)

    def test_get_third_index(self):
        test_data = "one and two and one again and two"
        result = lab8.get_third_index(test_data, "one")
        self.assertEqual(-1, result)
        result = lab8.get_third_index(test_data, "and")
        self.assertEqual(26, result)


if __name__ == '__main__':
    unittest.main()
