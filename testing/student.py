import unittest

class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id

class TestStudent(unittest.TestCase):
    def test_student(self):
        s = Student('Akash', 1)
        self.assertEqual((s.name, s.id), ('Akash', 1))

unittest.main()