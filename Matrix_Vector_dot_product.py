def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    #step 1 check if the number of columns in the matrix matches the size of the vector
    if len(a[0])==len(b) or len(a)==len(b):
        c=[]
        for i in a:
            hold=0
            for j in range(len(i)):
                hold+=i[j]*b[j]
            c.append(hold)
    else:
        c=-1
    print(c)
    return c
    
    
# Example usage
print(matrix_dot_vector([[1, 2], [3, 4]], [5, 6]))  # Output: [17, 39]
print(matrix_dot_vector([[1, 2], [3, 4]], [5, 6, 7]))  # Output: -1 (incompatible sizes)
print(matrix_dot_vector([[1, 2, 3], [4, 5, 6]], [7, 8, 9]))  # Output: [50, 122]