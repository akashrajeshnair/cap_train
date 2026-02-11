n = int(input("Enter size of list: "))
l = list(map(int, input("Enter ratings: ").split()))

def mysum(l):
    if len(l) == 0:
        return 0
    return l[0] + mysum(l[1:])

print(mysum(l))