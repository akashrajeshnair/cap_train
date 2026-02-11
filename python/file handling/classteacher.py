def sum_of_odd(n):
    mod = 10007
    total = 0

    for r in range(1, n+1):
        while r%2 == 0:
            r//=2
        total = (total+r)%mod

    return total

n = int(input("Enter number of students: "))
print(sum_of_odd(n))