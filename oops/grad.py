s = input("Enter the string: ").lower()

count = 0
for i, c in enumerate(s):
    if ord(c) == ord('a') + i:
        count += 1
    
print(count)