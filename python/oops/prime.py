n = int(input("Enter a number:"))

factors = []
for i in range(1, n//2+1):
    if n % i == 0:
        factors.append(i)
factors.append(n)

if sum(factors) == n+1:
    print("Number is prime")
else:
    print("Number is non-prime")