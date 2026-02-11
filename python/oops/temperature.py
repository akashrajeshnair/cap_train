n = input("Number of readings: ")
temps = list(map(int, input("Enter temparatures: ").split()))

def fix_temps(temps):
    return temps[::-1]

print(fix_temps(temps))