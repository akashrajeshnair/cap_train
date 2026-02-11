age = int(input("Enter age: "))
show = float(input("Enter show timing: "))

if show == 10.15 or show == 18.00 or show == 22.00:
    if age > 13:
        print("$2.00")
elif show == 13.30:
    print("$1.00")