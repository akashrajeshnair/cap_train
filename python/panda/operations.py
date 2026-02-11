import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
print(df.info())

print(df.isnull().sum())
df = df.fillna(0)

ages = df[df['age'] > 25]
print(ages)

df['total'] = df['a'] + df['b']
print(df.head())

res = df.groupby('category')['sales'].sum()
print(res)

