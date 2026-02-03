n = int(input("Enter size of matrix: "))

w = []
for i in range(n):
    w.append(list(map(int, input("Enter row").split())))

srs, scs = [], []
for i in range(n):
    sr = 0
    for j in range(n):
        sr += w[i][j]
    srs.append(sr)

for i in range(n):
    sc = 0
    for j in range(n):
        sc += w[j][i]
    scs.append(sc)

print("Sum of rows: ", *srs)
print("Sum of columns: ", *scs)