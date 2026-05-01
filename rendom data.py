import pandas as pd

df = pd.read_csv(r'C:\Users\Administrator\Desktop\Pandas\sales_data.csv')
df['total'] = df['quantity'] * df['price']
df['date'] = pd.to_datetime(df['date'])
print("Total revenue by product:")
print(df.groupby('product')['total'].sum())
print("\nBest selling day:")
print(df.groupby('date')['quantity'].sum().sort_values(ascending=False).head(1))
print("\nAverage price per product:")
print(df.groupby('product')['price'].mean())