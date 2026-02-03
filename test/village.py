s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

longest = ""
for i in range(len(s2)):
    for j in range(i, len(s2)+1):
        if s2[i:j] in s1 and len(s2[i:j]) > len(longest):
            longest = s2[i:j]
            print(longest)
print(longest)
sum = 0
for c in longest:
    sum += ord(c)

print(sum)