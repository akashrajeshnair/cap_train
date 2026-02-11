try:
    correct = 1234
    pin = int(input("Enter PIN Number: "))
    if pin != correct:
        raise ValueError
    else:
        print("Access Granted!")
except ValueError:
    print("Invalid PIN")