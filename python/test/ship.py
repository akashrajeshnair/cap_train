c = int(input("Enter capacity of the ship: "))
n = int(input("Enter number of people: "))

if n%50 == 0:
    print(n//c)
else:
    print((n//c)+1)