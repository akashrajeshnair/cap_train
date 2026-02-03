try:
    n = -5
    res = 100/n
except ZeroDivisionError:
    print("Cannot be divided by 0!")
except ValueError:
    print("Enter a valid Number")
else:
    print("Result is ", res)
finally:
    print("Execution complete!")