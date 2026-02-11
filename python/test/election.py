n = int(input("Enter number of voters: "))
a = list(map(int, input("Enter votes: ").split()))

parties = []

for p in a:
    if p not in parties:
        parties.append(p)

winner, maxi = 0, 0
for p in parties:
    c = 0
    for v in a:
        if v == p:
            c += 1
    if c > maxi:
        winner, maxi = p, c

print(winner) if maxi >= (n//2)+1 else print("-1")