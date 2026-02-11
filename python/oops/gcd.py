def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n1, n2 = map(int, input("Enter two numbers: ").split())
res = gcd(n1, n2)
print(f"The GCD of {n1} and {n2} is: {res}")
