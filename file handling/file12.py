try:
    file = open("test.txt", 'r')
    content = file.read()
    print(content)
finally:
    print("closing file.")
    file.close()