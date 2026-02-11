n = int(input("Enter number of seats: "))
a = list(map(int, input("Enter seating row: ").split()))

c = 0
for i in a:
    if i == 0:
        c += 1

print(c)