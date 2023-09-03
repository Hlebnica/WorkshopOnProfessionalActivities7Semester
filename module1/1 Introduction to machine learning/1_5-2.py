import numpy as np

k = int(input())

matrix = []
while True:
    try:
        row = input().strip().split()
        if not row:
            break
        matrix.append(list(map(int, row)))
    except EOFError:
        break

matrix = np.array(matrix)

result = []
for i in range(0, matrix.shape[0], k):
    for j in range(0, matrix.shape[1], k):
        block = matrix[i:i + k, j:j + k]
        result.append(np.sum(block))

result_rows = (matrix.shape[0] + k - 1) // k
result_cols = (matrix.shape[1] + k - 1) // k

result_matrix = np.array(result).reshape((result_rows, result_cols))
for row in result_matrix:
    print(" ".join(map(str, row)))