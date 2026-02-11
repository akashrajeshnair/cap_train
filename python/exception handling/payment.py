class CardError(Exception):
    pass

class PaymentError(Exception):
    pass

try:
    cardn = 1234567890
    n = int(input("Enter card number: "))
    if cardn != n:
        raise CardError
    try:
        b = int(input("Enter balance: "))
        w = int(input("Enter payment amount: "))
        if b-w < 0:
            raise PaymentError
        print("Payment Successfull")
    except PaymentError:
        print("Payment Failed")
except CardError:
    print("Invalid Card") 