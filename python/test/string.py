s = input("Enter string: ")

mini = []

letters = []
for c in s:
    if c not in letters:
        letters.append(c)

for l in letters:
    count = 0
    for c in s:
        if c != l:
            count += 1
    mini.append(count)

print(min(mini))

