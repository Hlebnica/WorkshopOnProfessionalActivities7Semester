import numpy as np
import pandas as pd

df = pd.read_csv('input.csv')

df = df.iloc[:, 1:]
data = df.values
max_values = np.max(data, axis=1)
column_with_most_max_values = np.argmax(np.sum(data == max_values[:, np.newaxis], axis=0))

print(column_with_most_max_values)