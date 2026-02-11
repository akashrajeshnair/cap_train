y = int(input("Enter a year: "))

def check_leap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True
    
while not check_leap(y):
    y += 1
    
print(y)