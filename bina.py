import pandas as pd
import numpy as np

data = np.zeros((121, 7))

with open('text.txt') as file:
    indx = 0
    for row in file:
        lst_text = list(map(float, row.split()))
        data[indx] = lst_text
        indx += 1

df = pd.DataFrame(data=data, columns=['Month', 'Year', 'Due', 'Principal', 'Interest', 'Insurance', 'Balance'])

df['Previous_Balance'] = df.Principal + df.Balance

df['%'] = 100 * (((df.Balance + df.Due - df.Insurance) / df.Previous_Balance) ** 12 - 1)

df_new = df[['Due', 'Principal', 'Interest', 'Insurance', 'Balance', 'Previous_Balance', '%']]


pd.set_option('display.max_rows', None)
print(df_new)