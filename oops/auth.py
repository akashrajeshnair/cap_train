n = int(input("Enter account number: "))

def count(n):
    if n < 10:
        return 1
    else:
        return 1 + count(n//10)
    
print(count(n))