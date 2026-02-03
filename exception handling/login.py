try:
    u = input("Enter username: ")
    p = input("Enter password: ")
    if len(u) == 0 or len(p) == 0:
        raise ValueError
    else:
        print("Username: ", u)
        print("Password: ", p)
except ValueError:
    print("Invalid Credentials") 