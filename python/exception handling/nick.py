n = int(input("Enter size of list; "))
l = list(map(int, input("Enter list: ").split()))

l.sort()
f = 1
for i in range(1, len(l)):
    if l[i] - l[i-1] != 1:
        f = 0
        break 

print(f)