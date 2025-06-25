def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    row=len(a)
    col=len(a[0]) if row > 0 else 0
    b=[]
    for i in range(col):
        new_row=[]
        for j in range(row):
            new_row.append(a[j][i]) 
        b.append(new_row)
    print(b)
    #step 3 return the transposed matrix
    return b
# Example usage 
print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))  # Output: [[1, 4], [2, 5], [3, 6]]
# Output: [[1, 4], [2, 5], [3, 6]]