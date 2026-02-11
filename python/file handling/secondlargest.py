n = int(input("Enter length of array: "))
a = list(map(int, input("Enter array elements: ").split()))

largest = 0
second_largest = 0
for i in range(n):
    if a[i] > largest:
        second_largest = largest
        largest = a[i]

count = 0
for i in range(n):
    if a[i] == second_largest:
        count += 1

print(count)