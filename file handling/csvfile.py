import csv
import io

csv_data = """Year,Industry,Value
2014,Manufacturing,697885
2014,Manufacturing,48000
2014,Manufacturing,12
"""

csv_file = io.StringIO(csv_data)
csvreader = csv.reader(csv_file)
for row in csvreader:
    print(row)