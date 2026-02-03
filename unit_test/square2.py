import unittest

def square(n):
    return n*n

class TestSquare(unittest.TestCase):
    def test_square_values(self):
        test_data = [
            (2,4),
            (3,9),
            (4,16),
            (5,25),
            (6,35)
        ]

        for num, expected in test_data:
            with self.subTest(num=num):
                self.assertEqual(square(num), expected)

unittest.main()