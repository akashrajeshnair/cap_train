def toh(n, s, d, a):
    if n == 1:
        print(f"{s} -> {d}")
        return
    toh(n-1, s, a, d)
    print(f"{s} -> {d}")
    toh(n-1, a, d, s)

n = int(input("Enter number of disks: "))
toh(n, 'A', 'C', 'B')