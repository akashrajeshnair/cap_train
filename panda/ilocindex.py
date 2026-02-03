import pandas as pd

df = pd.read_csv('employees.csv')
ser = pd.Series(df['First Name'])
data = ser.head(10)
print(data)