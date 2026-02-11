s = input("Enter a string: ")
n = int(input("Enter length of string: "))
c = input("Enter character: ")

count = 0
for x in s:
    if x == c:
        count += 1

print(count)