s = input("Enter log string: ")

prev = ''
compressed = ''
for c in s:
    if c != prev:
        compressed += c
        prev = c

print(compressed)