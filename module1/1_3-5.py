df = df.iloc[:, 1:]

correlations = df.corr().abs()

np.fill_diagonal(correlations.values, 0) 

max_correlations = correlations.max()
max_correlations = max_correlations.round(2).fillna(0.0)

result = max_correlations.tolist()

if len(result) == 1:
    result = [1.0]

print(result)