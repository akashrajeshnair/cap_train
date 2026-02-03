class BankAccount:
    def __init__ (self):
        self.balance = 100

    def _show_balance(self):
        print(f"balance: Rs{self.balance}")

    def __update_balance(self, amount):
        self.balance += amount

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            self._show_balance()
        else:
            print("Invalid amount")

account = BankAccount()
account._show_balance() # shows but bad practice
# account.__update_balance(300) # error
account.deposit(300)
