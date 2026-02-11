lines = ["Line 1", "Line 2", "Line 3"]
text = "\n".join(lines)+"\n"

with open("test4.txt", 'w') as f:
    f.write(text)

with open("test4.txt", 'r') as f:
    print(f.read())