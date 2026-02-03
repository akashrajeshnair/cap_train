import unittest

class Bank():
    def get_interest_rate():
        pass 

class SBI(Bank):
    def get_interest_rate(self):
        return "8%"
    
class HDFC(Bank):
    def get_interest_rate(self):
        return "7%"
    
class TestBank(unittest.TestCase):
    def test_sbi_interest(self):
        s = SBI()
        self.assertEqual(s.get_interest_rate(), "8%")

    def test_hdfc_interest(self):
        h = HDFC()
        self.assertEqual(h.get_interest_rate(), "7%")

unittest.main()