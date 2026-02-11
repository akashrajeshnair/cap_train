s = input("Enter string: ")
x = input("Enter character to be removed: ")

new = ""

for c in s:
    if c != x:
        new += c

print(new)