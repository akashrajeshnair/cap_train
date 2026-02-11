import unittest

def square(n):
    return n*n

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)

unittest.main()