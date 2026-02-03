import json

with open("test.json", 'r') as jsonfile:
    data = json.load(jsonfile)
    print(data)