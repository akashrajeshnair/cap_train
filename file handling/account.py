class BalanceError(Exception):
    pass

def checkBalance():
    try:
        bal = int(input("Enter balance: "))
        if bal != 0:
            raise BalanceError
        else:
            print("Account Closed")
    except BalanceError:
        print("caught error within function")
        raise

try:
    checkBalance()
except BalanceError:
    print("re-raised")
    print("Account has pending balance")
