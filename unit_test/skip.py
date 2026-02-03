import unittest
import pandas
import sys

def external_resource_available():
    return False

class MyTestCase(unittest.TestCase):
    @unittest.skip('Demonstrate skipping')
    def test_nothing(self):
        self.fail('should not happen')

    @unittest.skipIf(pandas.__version__ < (4), 'not supported in this library version')
    def test_format(self):
        pass

    @unittest.skipUnless(sys.platform.startswith("linux"), 'requires linux')
    def test_linux_support(self):
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest('external resource not available')
        pass

class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1,0,'broken')

def skipUnlessHasAttr(obj, attr):
    if hasattr(obj, attr):
        return lambda func:func
    return unittest.skip(f"{obj} doesn't have {attr}")

