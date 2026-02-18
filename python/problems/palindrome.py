m = int(input())
s = input()

s1 = ''
s2 = ''
out = 0

if len(s) % 2 == 0:
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
else:
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid + 1:]

for i in range(len(s1)):
    if s1[i] == '?' and s2[len(s2) - 1 - i] == '?':
        out += 26
        break
    elif s1[i] == '?' or s2[len(s2) - 1 - i] == '?':
        out += 1
    elif s1[i] != s2[len(s2) - 1 - i]:
        out = 0
        break

print(out % m)