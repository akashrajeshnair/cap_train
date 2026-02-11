m, n = map(int, input("Enter size of matrix: ").split())

qc = []
for i in range(m):
    qc.append(list(map(int, input(f"Enter row {i}: ").split())))


count = 0
for i in range(m):
    prev = -1001
    for j in range(n):
        if prev <= qc[i][j]:
            prev = qc[i][j]
        else:
            count += 1
            break

print(count)