import math

n = int(input("Enter size of array: "))
a = list(map(int, input("Enter array elements: ").split()))

mini = math.inf
for i in range(n):
    for j in range(i, n):
        if i != j:
            avg = (a[i]+a[j])/2
            s = 0
            for x in a:
                if x >= avg:
                    s += x
            if mini > s:
                mini = s

print(mini)


    
