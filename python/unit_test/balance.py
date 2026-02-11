import unittest

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError('Insufficient Balance')
    return amount - balance

def test_exception(self):
    with self.assertRaises(ValueError):
        withdraw(100,200)

class Bank:
    def deposit(self, amt):
        return amt

class TestBank(unittest.TestCase):
    def test_deposit(self):
        bank = Bank()
        self.assertEqual(bank.deposit(1000), 1000)

    @unittest.skip("Feature not ready")
    def test_future(self):
        pass

unittest.main()


