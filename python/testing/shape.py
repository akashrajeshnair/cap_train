import unittest

class Shape():
    def area():
        pass

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s*self.s
    
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l*self.b
    
class TestArea(unittest.TestCase):
    def test_square_area(self):
        s = Square(10)
        self.assertEqual(s.area(), 100)

    def test_rectangle_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

unittest.main()