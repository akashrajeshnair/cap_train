import unittest

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 5
    
    def test_add(self):
        self.assertEqual(self.a+self.b, 15)

    def tearDown(self):
        pass

unittest.main()


