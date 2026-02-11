n = int(input("Enter size of the image: "))
image = []

for i in range(n):
    image.append(list(map(int, input(f"Enter row {i}: ").split())))

for i in range(n):
    image[i].reverse()

for i in range(n):
    for j in range(n):
        if image[i][j] == 0:
            image[i][j] = 1
        elif image[i][j] == 1:
            image[i][j] = 0

for i in range(n):
    print(*image[i])