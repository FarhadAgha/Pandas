import pandas as pd
import matplotlib.pyplot as plt

data = {'city':['Qta', 'Lahore', 'Karachi'],
        'Sales':[250, 400, 350]}

df = pd.DataFrame(data)

plt.figure()
df.plot(x='city', y='Sales', kind='line', title='Line Plot')
plt.show()

plt.figure()
df.plot(x='city', y='Sales', kind='bar', title='Bar Plot')
plt.show()

plt.figure()
df.plot(y='Sales', kind='pie', labels=df['city'], autopct='%1.1f%%', legend=False)
plt.show()

plt.figure()
df.plot(kind='box', title='Box Plot')
plt.show()
