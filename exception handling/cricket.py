n = int(input("Enter number of overs: "))
l = [95.0]

for i in range(1, n):
    l.append(l[i-1]+20.5)

print(*l)