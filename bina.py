import pandas as pd
import numpy as np

data = np.zeros((120, 7))

with open('text.txt') as file:
    indx = 0
    for row in file:
        lst_text = list(map(float, row.split()))
        data[indx] = lst_text
        indx += 1

df = pd.DataFrame(data=data, columns=['Month', 'Year', 'Due', 'Principal', 'Interest', 'Insurance', 'Balance'])\

print(df)
