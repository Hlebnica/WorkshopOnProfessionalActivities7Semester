import numpy as np

matrix = []
while True:
    try:
        row = input().split()
        if not row:
            break
        matrix.append(list(map(int, row)))
    except EOFError:
        break

matrix = np.array(matrix)
    
num_zero_columns = np.sum(np.all(matrix == 0, axis=0))

print(num_zero_columns)