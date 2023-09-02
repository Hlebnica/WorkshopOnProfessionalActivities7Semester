import numpy as np

matrix = []
while True:
    try:
        row = input().split()
        if not row:
            break
        matrix.append(list(map(float, row)))
    except EOFError:
        break

matrix = np.array(matrix)
    
row_means = np.mean(matrix, axis=1, keepdims=True)

result_matrix = matrix - row_means

print(str(result_matrix))