import unittest

class Widget:
    def __init__(self):
        self.width = 50
        self.height = 50

    def resize(self, width, height):
        self.width = width
        self.height = height

class WidgetTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget()
        self.assertEqual(widget.width, 50)
        self.assertEqual(widget.height, 50)

    def test_widget_resize(self):
        widget = Widget()
        widget.resize(100,150)
        self.assertEqual(widget.width, 100)
        self.assertEqual(widget.height, 150)

unittest.main()