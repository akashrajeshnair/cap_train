i = int(input("Enter investment: "))
l = int(input("Enter earnings: "))

if i < 0 or l < 0:
    print("Invalid input")
else:
    x = ((l-i)*100)/i
    if x < 0:
        print(f"Loss of {x}%")
    else:
        print(f"Profit of {x}%")