s = input("Enter a string: ")

if len(s) == 0:
    print("-1")
else:
    count = 0
    for c in s:
        if c.isalnum():
            count += 1

print(count)