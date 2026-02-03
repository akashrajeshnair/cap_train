try:
    x = int("str")
    inv = 1/x
except ValueError:
    print("Not valid!")
except ZeroDivisionError:
    print("Zero has no inverse")