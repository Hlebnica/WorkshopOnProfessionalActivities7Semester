import numpy as np

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

print(len(np.unique(matrix, axis=0)))