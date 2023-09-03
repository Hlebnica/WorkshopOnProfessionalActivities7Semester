df = df.iloc[:, 1:]
print((df == 1).sum().sum())