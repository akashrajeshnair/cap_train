n = int(input("Enter n: "))
m = []
for i in range(n):
    m.append(list(map(int, input(f"Enter row {i}: ").split())))

maxs = []
for i in range(n):
    maxc = 0
    for j in range(n):
        if m[j][i] > maxc:
            maxc = m[j][i]
    maxs.append(maxc)

print(*maxs)