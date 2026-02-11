n = int(input("Enter number of houses: "))
a = list(map(int, input("Enter stairs: ").split()))

count = 0
for i in a:
    if i%3 == 0:
        count += 1
        