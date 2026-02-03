n = int(input("Enter number of chocolate types: "))
k = int(input("Enter number of types of chocolate to buy: "))
t = list(map(int, input("Enter types of chocolates: ").split()))
p = list(map(int, input("Enter prices of chocolates: ").split()))

max_type = max(t)
minp = [float("inf")]*(max_type+1)

for i in range(n):
    if p[i] < minp[t[i]]:
        minp[t[i]] = p[i]

prices = []
for i in range(1, max_type+1):
    if minp[i] != float("inf"):
        prices.append(minp[i])


if len(prices) < k:
    print(-1)
else:
    prices.sort()
    total = sum(prices[:k])
    print(total)