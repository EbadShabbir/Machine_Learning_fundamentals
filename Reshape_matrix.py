import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #step 1 get the number of rows and columns in the original matrix
    m= len(a)
    n = len(a[0]) if m > 0 else 0
    
    #step 2 check if the it is feasible to reshape the matrix
    if m * n != new_shape[0] * new_shape[1]:
        return []
    #step 3 create a new matrix with the desired shape
    reshaped_matrix = [[0] * new_shape[1] for _ in range(new_shape[0])]

    #step 4 fill the new matrix with elements from the original matrix
    flat_postion = 0
    for i in range(m):
        for j in range(n):
            current_value = a[i][j]
            new_row = flat_postion // new_shape[1]
            new_col = flat_postion % new_shape[1]
            reshaped_matrix[new_row][new_col] = current_value
            flat_postion += 1   
    return reshaped_matrix
print(reshape_matrix([[1, 2], [3, 4]], (1, 4)))  # Example usage