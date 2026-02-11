n = int(input("Enter size of the matrix"))
power = []
for i in range(n):
    power.append(list(map(int, input(f"Enter row {i}: ").split())))

d1 = 0
for i in range(n):
    d1 += power[i][i]

d2 = 0
for i in range(n):
    for j in range(n-1, 0, -1):
        d2 += power[i][j]

print(d1, d2)