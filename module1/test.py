import numpy as np
import pandas as pd

#df = pd.read_csv(input.csv)

data = {'A': [1, 2, None, 4],
        'B': [None, 2, 3, 4],
        'C': [1, 2, 3, 4]}
df = pd.DataFrame(data)

has_missing_values = df.isna().any().any()
print(has_missing_values)