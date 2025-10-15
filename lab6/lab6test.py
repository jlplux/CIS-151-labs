import unittest

import lab6



class MyTestCase(unittest.TestCase):

   def test_is_vowel(self):

       self.assertTrue(lab6.is_vowel("a"))

       self.assertFalse(lab6.is_vowel("w"))

       self.assertFalse(lab6.is_vowel("ae"))



   def test_filter_vowels(self):

       result = lab6.filter_vowels("hello")

       self.assertEqual("eo", result)

       result = lab6.filter_vowels("qweraasdfi")

       self.assertEqual("eaai", result)



   def test_contains(self):

       list_data = [1, 23, 5, 88, 29]

       self.assertTrue(lab6.contains(list_data, 1))

       self.assertTrue(lab6.contains(list_data, 23))

       self.assertTrue(lab6.contains(list_data, 29))

       self.assertFalse(lab6.contains(list_data, 2))

       self.assertFalse(lab6.contains(list_data, 20))



   def test_index_of(self):

       list_data = [1, 23, 5, 88, 29]

       result = lab6.index_of(list_data, 1)

       self.assertEqual(0, result)

       result = lab6.index_of(list_data, 23)

       self.assertEqual(1, result)

       result = lab6.index_of(list_data, 29)

       self.assertEqual(4, result)



   def test_get_login(self):

       result = lab6.get_login("jane", "doe")

       self.assertEqual("jdoe", result)

       result = lab6.get_login("joseph", "longlastname")

       self.assertEqual("jlongl", result)



   def test_get_padded_login(self):

       result = lab6.get_padded_login("jane", "doe")

       self.assertEqual("jdoe00", result)

       result = lab6.get_padded_login("joseph", "longlastname")

       self.assertEqual("jlongl", result)





if __name__ == '__main__':

   unittest.main()

