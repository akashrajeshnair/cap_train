n = int(input("Enter number of elements: "))
l = list(map(int, input("Enter the elements: ").split()))

new = l.copy()
avgs = []
minsum = float('inf')
for i in range(n):
    for j in range(i+1, n):
        avg = (l[i] + l[j]) / 2
        avgs.append(avg)
        
for avg in avgs:
    for i in range(len(new)):
        if avg < new[i]:
            new[i] = 0
    minsum = min(minsum, sum(new))
    new = l.copy()

print(int(minsum))