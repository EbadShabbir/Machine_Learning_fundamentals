import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    """
    Calculates the mean of a matrix by row or column, corrected to use the user's
    variable definitions and logic.
    """
    # Handle empty matrix case to prevent errors
    if not matrix or not matrix[0]:
        return []

    # --- Using your variable names as you defined them ---
    # NOTE: Your 'col' variable actually stores the number of rows.
    col = len(matrix) 
    # NOTE: Your 'rows' variable actually stores the number of columns.
    rows = len(matrix[0])
    
    # We will perform the calculations with Python loops as requested.
    # The numpy lines are not needed for this approach.
    means = []

    if mode == 'row':
        # Corrected row calculation
        for i in range(col): # This correctly loops through each row index
            # Sum the current row (matrix[i]) and divide by the number of columns ('rows' variable)
            # Use standard division '/' for an accurate float result.
            row_mean = sum(matrix[i]) / rows
            means.append(row_mean)
            
    elif mode == 'column':
        # Corrected column calculation
        # The outer loop must iterate through the column indices, which is range(rows).
        for col_index in range(rows):
            
            # This list comprehension builds a list of all values from the current column.
            # The typo 'for rows in matrix' has been fixed to 'for row in matrix'.
            column_values = [row[col_index] for row in matrix]
            
            # Calculate the sum of the extracted column values.
            column_sum = sum(column_values)
            
            # Divide by the number of rows (stored in your 'col' variable).
            # The undefined variable 'num_rows' is replaced with 'col'.
            column_mean = column_sum / col
            
            # Append the calculated mean to your results list.
            means.append(column_mean)

    else:
        print("Error: Invalid mode. Please use 'row' or 'column'.")

    return means
#EXAMPLE USAGE
print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'row'))      # Output: [2.0, 5.0, 8.0]
print(calculate_matrix_mean([[1, 2, 3], [4, 5   , 6], [7, 8, 9]], 'column'))   # Output: [4.0, 5.0, 6.0]