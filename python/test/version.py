n = int(input("Enter number of files: "))
s = input("Enter filenames: ")

sa = s.split()

v = 0
try:
    for f in sa:
        fv = int(f[5:])
        if fv > v:
            v = fv
    print(v)
except ValueError:
    print("-1")
