import pandas as pd
df = pd.read_csv('fruits.csv')
df['earnings'] = df['price'] * df['kg_sold']

print("Fruit Stand Report")
print("-" * 30)
print(df)
print("-" * 30)
print(f"Total earnings: ${df['earnings'].sum()}")
print(f"Best selling fruit: {df.loc[df['kg_sold'].idxmax(), 'fruit']}")
print(f"Most expensive fruit: ${df['price'].max()}")