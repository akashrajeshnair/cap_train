import pytest

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, dep):
        self.__balance += dep
        return self.__balance
    
    def withdraw(self, wit):
        self.__balance -= wit
        return self.__balance
    

b = BankAccount()
def test_deposit():
    assert b.deposit(100) == 100
    
def test_withdraw():
    assert b.withdraw(100) == 0