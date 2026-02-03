import unittest

class FloatTestCase(unittest.TestCase):
    def test_division(self):
        data = [
            (1,2,0.5),
            (1,4,0.25),
            (1,10,0.1)
        ]

        for a, b, expected in data:
            with self.subTest(a=a, b=b):
                self.assertEqual(a/b, expected)

unittest.main()