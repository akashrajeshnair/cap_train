try:
    age = int(input("Enter age: "))
    if age < 0:
        raise Exception
    else:
        print(age)
except Exception:
    print("Invalid age")