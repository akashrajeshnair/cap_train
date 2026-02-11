s = input("Enter a string: ")

words = []
word = ""
for c in s:
    if c != " ":
        word += c
    else:
        words.append(word)
        word = ""
words.append(word)

words.reverse()
print(*words)