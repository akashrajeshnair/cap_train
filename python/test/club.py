n = int(input("Enter number of members: "))
s = input("Enter string: ")

sa = s.split()
res = ""
for p in sa:
    res += p[0].upper()

print(res)