n = int(input("Enter number of terms: "))

series = [1, 3]
series.append(series[0]+series[1])
for i in range(3, n):
    series.append(series[len(series)-3]+series[len(series)-2]+series[len(series)-1])

print(*series)