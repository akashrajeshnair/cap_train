try:
    with open("test3.txt", 'x') as f:
        f.write("Created using exclusive mode.\n")
except FileExistsError:
    print("file already exists, exclusive creation aborted.")