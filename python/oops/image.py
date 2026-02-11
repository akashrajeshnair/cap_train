n = int(input("Enter size of image: "))

image = []
for i in range(n):
    image.append(list(map(int, input(f"Enter row {i}: ").split())))


new = []
for i in range(n):
    new.append([])
cols = []

for j in range(n):
    col = []
    for i in range(n):
        col.append(image[j][i])
    cols.append(col)

new = [list(reversed(cols)) for col in cols]
print(*new)
# for i in range(n):
#     for j in range(n):
#         print(new[i][j])
#     print("\n")