import unittest

class Widget():
    def __init__(self, name):
        self.name = name
    
    def size(self):
        return (50,50)

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50,50))

unittest.main()