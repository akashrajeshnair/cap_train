class AuthenticationError(Exception):
    pass

class BalanceError(Exception):
    pass

try:
    username = "user"
    password = "1234"
    u = input("Enter username: ")
    p = input("Enter password: ")
    if u != username or p != password:
        raise AuthenticationError
    b = int(input("Enter balance: "))
    w = int(input("Enter withdrawal amount: "))
    if b-w < 0:
        raise BalanceError
    else:
        print("Transaction successfull")
except AuthenticationError:
    print("Authentication failed")
except BalanceError:
    print("Insufficient Balance")
finally:
    print("Session Closed")

