n = int(input('Enter number of students: '))
m = input('Enter an integer: ')
a = list(map(str, input('Enter the marks of students: ').split()))

nums = []
for i in m:
    if i not in nums:
        nums.append(int(i))
s = min(nums)
passed = 0
passing = True
for marks in a:
    su = 0
    for i in marks:
        su += int(i)
        if int(i) in nums:
            passing = False
    if su >= s and passing:
        passed += 1

print(passed)