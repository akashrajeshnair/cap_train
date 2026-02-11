import unittest

class Widget():
    def __init__(self, name):
        self.name = name
    
    def size(self):
        return (50,50)
    
    def resize(self, n):
        return (50*n, 50*n)

class WidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50,50))
    
    def test_widget_resize(self):
        widget = Widget('The widget')
        self.assertEqual(widget.resize(3), (150, 150))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetSizeTestCase('test_default_widget_size'))
    suite.addTest(WidgetSizeTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())