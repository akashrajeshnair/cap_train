def dtob(n):
    if n < 2:
        return str(n)
    else:
        return dtob(n // 2) + str(n % 2)
    
n = int(input("Enter number: "))
b = dtob(n)
count = 0
for c in str(b):
    if c == '1':
        count += 1

print(count)
    