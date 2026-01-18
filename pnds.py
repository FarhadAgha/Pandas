'''                     / These all are simple codes solving simple problems using Pandas Library /                      '''

import pandas as pd
data = {'Name': ['Ali', 'Ahmed', 'Abid'], 
        'Age': [22,44,65],
        'Marks': [99, 100, 50]}
df = pd.DataFrame(data)
print(df)
print()
print(df[df['Marks'] > 80])
print()
print(df[df['Age'] < 30])
print(df.loc[0:2,['Name','Marks']])
print(df['Age'].unique())
print(df['Age'].value_counts())
print(df.sort_values(by='Marks', ascending=False))

'''                     //                    '''
import pandas as pd
data = {'Name': ['Noman', 'Ali', 'Usman', 'Fatima'],
        'Age': [22,21,21,24],
        'Marks': [88, 66,53,88]}
df = pd.DataFrame(data)
print(df)
print()
print(df.isnull())
print(df.isnull().sum())

'''                     //                      '''

import pandas as pd
df1 = pd.DataFrame({'ID': [1,2,3],
                    'Name': ['ALi', 'Ahmed', 'Omer'],
                    'City': ["NewYourk", "Berlin", "Framkfort"]})
df2 = pd.DataFrame({'ID': ["a","b","c"],
                    'City': ['Qta', 'Lahore', 'Karachi'],
                    'Name': ["Farhad", "Fatma", "Aliay"]})
concat_df = pd.concat([df1, df2], axis=1)
print("Concatenation:\n", concat_df)
print()
concat_df1 = pd.concat([df1, df2], axis=0)
print("Concatenation:\n", concat_df1)

'''                     //                      '''

import pandas as pd
df1 = pd.DataFrame({'ID': [1,2,3],
                    'Name': ["Farhad", "Ali", "Ahmed"]})
df2 = pd.DataFrame({'ID': [2,4,3],
                    'City': ["Berlin", "Frankfort", "DeutchLand"]})
inner_merge = pd.merge(df1, df2, on='ID', how='inner')
print("\ninner Join:\n", inner_merge)

'''             //              '''

import pandas as pd
Data = pd.DataFrame({'Name': ['Ali', 'Ayesha', 'Usman', 'Sara'], 
                     'Age': [15, 16, 15, 14],
                     'Grade': ['A', 'B', 'A', 'C']})
print("Original DataFrame:\n", Data)
print()

'''                     //              '''

import pandas as pd
data = pd.DataFrame({'ID': [1,2,3,4],
         'Name': ['Ali', 'Ayesha', 'Usman', 'Sara'],
         'age': [15,16,15,14],
         'Grade': ['A', 'B', 'A', 'C']})
print("Original DataFrame:\n", data)
print()
print("\nColumns:", data.columns)
print("\nNames and Grades:")
print(data[['Name', 'Grade']])
print("\nAverage age:", data['age'].mean())
print("Sort by Age:")
print(data.sort_values(by='age'))
print("students with A Grade:")
print(data[data['Grade'] == 'A'])

'''                     //                      '''

import pandas as pd
df_products = pd.DataFrame({'Product ID': [1,2,3],
                            'Product Name': ['Laptop', 'Phone', 'Chair'],
                            'Price': [120000, 80000, 5000]})
df_sales = pd.DataFrame({'Sale ID': [101, 102, 103],
                         'Product ID': [1, 3, 2],
                         'Quantity': [2, 3, 1]})
marged = pd.merge(df_products, df_sales, on='Product ID')
marged['TotalValue'] = marged['Price'] * marged['Quantity']
print(df_products)

print(marged)
