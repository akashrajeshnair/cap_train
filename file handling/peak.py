n = int(input("Enter size of array: "))
a = list(map(int, input("Enter array values: ").split()))

peak = 0

for i in range(n):
    if a[i] > peak:
        peak = a[i]

print(peak)