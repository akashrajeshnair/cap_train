try:
    a, b = map(int, input("Enter two numbers: ").split())
    print(a/b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Division by 0 is not allowed")