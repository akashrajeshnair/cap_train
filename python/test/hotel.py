n = int(input("Enter the number of reserved rooms: "))
a = list(map(int, (input("Enter the array of reserved rooms: ")).split()))
t = int(input("Enter the total number of rooms: "))

print(t-n)