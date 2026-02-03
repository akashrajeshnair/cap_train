n = int(input("Enter number of items: "))
b = list(map(int, input("Enter items: ").split()))

p = 0
for i in b:
    if i%7 == 0:
        if p == 0:
            p = 1
        p *= i

print(p)
