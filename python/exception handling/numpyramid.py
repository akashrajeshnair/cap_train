s = 10
for i in range(4, 0, -1):
    for j in range(i):
        print(f"{s}*", end="")
        s -= 1
    print("", end="\n")