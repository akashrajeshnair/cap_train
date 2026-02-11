n = int(input("Enter number: "))
k = int(input("Enter digit: "))

if k > len(str(n)):
    print("-1")
else:
    print(str(n)[k-1])