try:
    m = int(input("Enter marks: "))
    if m > 100:
        raise ValueError
    else:
        print("Valid Marks")
except ValueError:
    print("Invalid Marks")