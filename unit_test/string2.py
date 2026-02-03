import unittest

class TestStringLength(unittest.TestCase):
    def test_string_length(self):
        strings = {
            'apple': 5,
            'banana': 6,
            'cat': 3,
            'dog': 4
        }

        for text, length in strings.items():
            with self.subTest(string=text):
                self.assertEqual(len(text), length)

unittest.main()