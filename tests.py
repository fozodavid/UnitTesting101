import unittest
from vowelsCheck import vowelsCheck


class TestVowelFunction(unittest.TestCase):

    def setUp(self):
        self.expected = {}

    def test_empty_string(self):
        result = vowelsCheck('')
        self.assertEqual(result, self.expected)

    def test_all_consonants(self):
        string = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        self.expected['consonants'] = 42
        result = vowelsCheck(string)
        self.assertEqual(result, self.expected)

    def test_all_vowels(self):
        string = "aeiouAEIOU"
        self.expected['a'] = 2
        self.expected['e'] = 2
        self.expected['i'] = 2
        self.expected['u'] = 2
        self.expected['o'] = 2
        result = vowelsCheck(string)
        self.assertEqual(result, self.expected)

    def test_symbols(self):
        string = "_+-&@$Ł!)(\/%"
        result = vowelsCheck(string)
        self.assertEqual(result, self.expected)

    def test_mixed_chars(self):
        string = "18Mixed_Characters"
        expected = {'a': 2, 'e': 2, 'i': 1, 'consonants': 10}
        result = vowelsCheck(string)
        self.assertEqual(result, expected)

    def test_input_not_a_string(self):
        input_list = [1, 3.14, ['item1', 'item2'], (1, 2), b'hello']
        for item in input_list:
            with self.assertRaises(TypeError):
                vowelsCheck(item)


if __name__ == '__main__':
    unittest.main()
