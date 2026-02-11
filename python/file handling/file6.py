file = open("test.txt", 'r')
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()
file.close()