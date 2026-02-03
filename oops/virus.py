n = int(input("Enter number of days: "))

rate = [2]
for i in range(1, n):
    rate.append(rate[len(rate)-1] + (13*i))

print(*rate)