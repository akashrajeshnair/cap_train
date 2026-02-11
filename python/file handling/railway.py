class SeatError(Exception):
    pass

try:
    n = input("Enter your name: ")
    req = int(input("Enter number of tickets: "))
    if req <= 0:
        raise ValueError
    av = int(input("Enter number of seats available: "))
    if req > av:
        raise SeatError
    print("Transaction Complete")
except ValueError:
    print("Ticket number must be greater than 0.")
except SeatError:
    print("Requested tickets exceed available seats.")