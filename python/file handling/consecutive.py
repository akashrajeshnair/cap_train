a = list(map(int, input("Enter array of integers: ").split()))

diff = []
for i in range(1, len(a)):
    diff.append(a[i]- a[i-1])

print(*diff)