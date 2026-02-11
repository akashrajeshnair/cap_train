try:
    w = int(input("Enter withdrawal amount: "))
    if w > 25000:
        raise Exception
    else:
        print("Withdrawal allowed")
except Exception:
    print("Daily limit exceeded.")
    