def tower_of_hanoi(n, src, dest, aux):
    if n == 1:
        print(f"{src} -> {dest}")
        return
    tower_of_hanoi(n-1, src, aux, dest)
    print(f"{src} -> {dest}")
    tower_of_hanoi(n-1, aux, dest, src)

n = int(input("Enter number of disks: "))
tower_of_hanoi(n, 'A', 'C', 'B')