n = int(input("Enter n: "))
terms = [1]
for i in range(1, n):
    t = []
    prev = terms[i-1]%10
    cur = 0
    for j in range(i+1):
        cur += (prev+1)*(10**(j-(i+1)))
        prev = prev+1
    print(cur)
    terms.append(cur)

print(*terms)