class InsufficientBalance(Exception):
    pass

balance = int (input("Enter balance: "))
try:
    w = int(input("Enter withdrawal amount: "))
    if w <= balance:
        print("Withdrawal Successful")
    else:
        raise InsufficientBalance
except ValueError:
    print("Invalid amount")
except InsufficientBalance:
    print("Insufficient Balance")