n = int(input("Enter number of problems: "))
p = int(input("Enter travel time: "))

t = 240 - p
s = 0
i = 1
c = 0
while s+(5*i) < t and c < n:
    s += 5*i
    i += 1
    c += 1

print(c)