import unittest

def divide(a,b):
    if b == 0:
        raise ValueError("Divison by 0")
    return a/b

class TestDivide(unittest.TestCase):
    def test_division(self):
        test_cases = [
            (10,2,5),
            (20,4,5)
        ]

        for a, b, result in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(divide(a,b), result)

    def test_division_by_zero(self):
        for b in [0]:
            with self.subTest(b=b):
                self.assertRaises(ValueError, divide, 10, b)

unittest.main()