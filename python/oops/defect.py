m, n = map(int, input("Enter m and n: ").split())

prod = []
for i in range(m):
    prod.append(list(map(int, input(f"Enter row {i}: ").split())))

maxa = []
for i in range(m):
    maxi = 0
    for j in range(n):
        maxi = prod[i][j] if prod[i][j] > maxi else maxi
    maxa.append(maxi)

print(*maxa)