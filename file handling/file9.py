with open("test.txt", 'a') as f:
    f.write("Appended Line\n")

with open("test.txt", 'r') as f:
    print(f.read())