def p2(n):
    if n == 0:
        return 1
    else:
        return 2*p2(n-1)
    
n = int(input("Enter number: "))
print(p2(n))