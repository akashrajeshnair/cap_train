import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_strings_a(self):
        self.assertEqual('a'*4, 'aaaa')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_strip(self):
        s = 'jayamamam'
        self.assertEqual(s.strip('jaya'), 'jayanan')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

unittest.main()