try:
    bal = int(input("Enter balance: "))
    w = int(input("Enter withdrawal amount: "))
    if bal-w < 1000:
        raise ValueError
    else:
        bal -= w
        print("Transaction successful")
except ValueError:
    print("Minimum Balance Violation")