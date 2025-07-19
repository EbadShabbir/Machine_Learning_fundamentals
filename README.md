# Matrix Operations Library

A comprehensive Python library for fundamental matrix operations including reshaping, matrix-vector multiplication, and matrix transposition. This library provides efficient implementations of core linear algebra operations with clear error handling and step-by-step algorithms.

## 🚀 Features

- **Matrix Reshaping**: Transform matrices into different dimensions while preserving element order
- **Matrix-Vector Multiplication**: Compute dot product between matrices and vectors with dimension validation
- **Matrix Transposition**: Convert rows to columns and vice versa efficiently
- **Matrix Mean Calculation**: Calculate mean values by row or column
- **Matrix Multiplication with Scalar**: Multiplying the scalar by the matrix
- **Eigenvalues Calculation**: Compute eigenvalues for 2x2 matrices using characteristic equation
- **Robust Error Handling**: Comprehensive validation for incompatible operations
- **Type Hints**: Full type annotation support for better code clarity

## 📋 Requirements
```
pip install numpy
```

## 💻 Complete Implementation

```
import numpy as np
from typing import List, Tuple, Union

def reshape_matrix(a: List[List[Union[int, float]]], new_shape: Tuple[int, int]) -> List[List[Union[int, float]]]:
    """
    Reshapes a 2D matrix into a new shape while maintaining the same total number of elements.
    
    Args:
        a: Input matrix to reshape
        new_shape: Target dimensions as (rows, columns)
    
    Returns:
        Reshaped matrix, or empty list [] if reshaping is impossible
    """
    if not a or not a:
        return []
    
    original_rows, original_cols = len(a), len(a)
    new_rows, new_cols = new_shape
    
    # Feasibility check
    if original_rows * original_cols != new_rows * new_cols:
        return []
    
    # Flatten the matrix using flat indexing
    flattened = []
    for i in range(original_rows):
        for j in range(original_cols):
            flattened.append(a[i][j])
    
    # Reshape using mathematical formulas
    result = []
    for i in range(new_rows):
        row = []
        for j in range(new_cols):
            flat_position = i * new_cols + j
            row.append(flattened[flat_position])
        result.append(row)
    
    return result

def matrix_dot_vector(a: List[List[Union[int, float]]], b: List[Union[int, float]]) -> Union[List[Union[int, float]], int]:
    """
    Performs matrix-vector multiplication (dot product) with dimension checking.
    
    Args:
        a: Input matrix (m×n)
        b: Input vector (length n)
    
    Returns:
        Result vector of length m, or -1 if dimensions are incompatible
    """
    if not a or not a or not b:
        return -1
    
    matrix_cols = len(a)
    vector_length = len(b)
    
    # Dimension validation
    if matrix_cols != vector_length:
        return -1
    
    # Dot product computation
    result = []
    for row in a:
        dot_product = sum(row[i] * b[i] for i in range(len(row)))
        result.append(dot_product)
    
    return result

def transpose_matrix(a: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """
    Transposes a matrix by swapping rows and columns.
    
    Args:
        a: Input matrix to transpose
    
    Returns:
        Transposed matrix
    """
    if not a or not a:
        return []
    
    rows, cols = len(a), len(a)
    
    # Element mapping: matrix[i][j] to transposed[j][i]
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(a[i][j])
        result.append(new_row)
    
    return result

def calculate_matrix_mean(matrix: List[List[float]], mode: str) -> List[float]:
    """
    Calculates the mean of a matrix by row or column.
    
    Args:
        matrix: Input matrix for mean calculation
        mode: Either 'row' or 'column' to specify calculation direction
    
    Returns:
        List of calculated means, or empty list [] for invalid input
    """
    if not matrix or not matrix:
        return []
    
    if mode not in ['row', 'column']:
        print("Error: mode must be 'row' or 'column'")
        return []
    
    result = []
    
    if mode == 'row':
        # Row mode: calculate mean for each row
        for row in matrix:
            row_mean = sum(row) / len(row)
            result.append(row_mean)
    
    elif mode == 'column':
        # Column mode: calculate mean for each column
        num_cols = len(matrix)
        for col_idx in range(num_cols):
            column_values = [row[col_idx] for row in matrix]
            col_mean = sum(column_values) / len(column_values)
            result.append(col_mean)
    
    return result

def calculate_scalar_multiplication(matrix: List[List[float]], scalar: int) -> List[List[float]]:
    """
    Calculates the multiplication of a matrix by scalar.
    
    Args:
        matrix: Input matrix for calculation
        scalar: Scalar multiplier value
    
    Returns:
        Resulting matrix after scalar multiplication
    """
    if not matrix or not matrix:
        return []
    
    # Flatten the matrix
    flattened = []
    for row in matrix:
        for element in row:
            flattened.append(element * scalar)
    
    # Unflatten back to matrix structure
    rows, cols = len(matrix), len(matrix)
    result = []
    
    for i in range(rows):
        new_row = []
        for j in range(cols):
            flat_index = i * cols + j
            new_row.append(flattened[flat_index])
        result.append(new_row)
    
    return result

def eigenvalues_calculation(A: List[List[float]]) -> List[float]:
    """
    Calculates eigenvalues of a 2x2 matrix using the characteristic equation.
    
    Args:
        A: Input 2x2 matrix
    
    Returns:
        List of eigenvalues [λ₁, λ₂]
    """
    if len(A) != 2 or len(A) != 2:
        raise ValueError("Matrix must be 2x2")
    
    # Extract matrix elements
    a, b = A, A
    c, d = A, A
    
    # Calculate trace and determinant
    trace = a + d
    determinant = a * d - b * c
    
    # Calculate discriminant
    discriminant = trace**2 - 4 * determinant
    
    # Calculate eigenvalues using quadratic formula
    sqrt_discriminant = discriminant**0.5
    lambda1 = (trace + sqrt_discriminant) / 2
    lambda2 = (trace - sqrt_discriminant) / 2
    
    return [lambda1, lambda2]
```

## 📚 Functions Documentation

### 1. `reshape_matrix(a, new_shape)`

Reshapes a 2D matrix into a new shape while maintaining the same total number of elements using flat indexing methodology.

**Algorithm:**
1. **Feasibility Check**: Verifies `original_rows × original_cols = new_rows × new_cols`
2. **Flat Indexing**: Maps each position using mathematical formulas:
   - `new_row = flat_position // new_columns`
   - `new_col = flat_position % new_columns`

**Parameters:**
- `a` (list[list[int|float]]): Input matrix to reshape
- `new_shape` (tuple[int, int]): Target dimensions as (rows, columns)

**Returns:**
- `list[list[int|float]]`: Reshaped matrix, or empty list `[]` if reshaping is impossible

### 2. `matrix_dot_vector(a, b)`

Performs matrix-vector multiplication (dot product) with comprehensive dimension checking.

**Algorithm:**
1. **Dimension Validation**: Ensures matrix columns match vector length
2. **Dot Product Computation**: For each matrix row, computes sum of element-wise products

**Parameters:**
- `a` (list[list[int|float]]): Input matrix (m×n)
- `b` (list[int|float]): Input vector (length n)

**Returns:**
- `list[int|float]`: Result vector of length m, or `-1` if dimensions are incompatible

### 3. `transpose_matrix(a)`

Transposes a matrix by swapping rows and columns using element mapping.

**Algorithm:**
1. **Dimension Analysis**: Determines original matrix dimensions
2. **Element Mapping**: Maps `matrix[i][j]` to `transposed[j][i]`

**Parameters:**
- `a` (list[list[int|float]]): Input matrix to transpose

**Returns:**
- `list[list[int|float]]`: Transposed matrix

### 4. `calculate_matrix_mean(matrix, mode)`

Calculates the mean of a matrix by row or column using pure Python implementation.

**Algorithm:**
1. **Input Validation**: Checks for empty matrix and valid mode
2. **Row Mode**: For each row, sums all elements and divides by number of columns
3. **Column Mode**: For each column, extracts values using list comprehension and calculates mean

**Parameters:**
- `matrix` (list[list[float]]): Input matrix for mean calculation
- `mode` (str): Either 'row' or 'column' to specify calculation direction

**Returns:**
- `list[float]`: List of calculated means, or empty list `[]` for invalid input

### 5. `calculate_scalar_multiplication(matrix, scalar)`

Calculates the multiplication of a matrix by scalar using pure Python implementation.

**Algorithm:**
1. **Flatten**: First flatten the matrix
2. **Scalar Multiply**: Multiply each element with the scalar and append to new list
3. **Unflatten**: Convert flattened result back to matrix structure

**Parameters:**
- `matrix` (list[list[float]]): Input matrix for calculation
- `scalar` (int): Scalar multiplier value

**Returns:**
- `list[list[float]]`: Resulting matrix after scalar multiplication

### 6. `eigenvalues_calculation(A)`

Calculates eigenvalues of a 2x2 matrix using the characteristic equation.

**Algorithm:**
1. **Matrix Elements Extraction**: Extracts elements a, b, c, d from 2x2 matrix
2. **Trace and Determinant**: Computes trace (`tr = a + d`) and determinant (`det = a*d - b*c`)
3. **Discriminant Calculation**: Computes `D = tr² - 4*det`
4. **Eigenvalues Calculation**:
   - `λ₁ = (tr + √D)/2`
   - `λ₂ = (tr - √D)/2`

**Parameters:**
- `A` (list[list[float]]): Input 2x2 matrix

**Returns:**
- `list[float]`: List of eigenvalues [λ₁, λ₂]

**Limitations:**
- Currently only supports 2x2 matrices

## ⚡ Performance Characteristics

| **Operation** | **Time Complexity** | **Space Complexity** |
|---------------|---------------------|----------------------|
| Matrix Reshape | O(m × n) | O(m × n) |
| Matrix-Vector Multiplication | O(m × n) | O(m) |
| Matrix Transpose | O(m × n) | O(m × n) |
| Matrix Mean Calculation | O(m × n) | O(max(m, n)) |
| Matrix Scalar Multiplication | O(m × n) | O(m × n) |
| Eigenvalues Calculation | O(1) | O(1) |

Where `m` = number of rows, `n` = number of columns

## 🔍 Error Handling

- **Reshape**: Returns empty list `[]` if reshaping is impossible due to incompatible dimensions
- **Matrix-Vector Multiplication**: Returns `-1` if matrix columns don't match vector length
- **Transpose**: Handles empty matrices gracefully with proper dimension checking
- **Mean Calculation**: Returns empty list `[]` for invalid input and prints error for invalid mode
- **Scalar Multiplication**: No error cases (handles all valid matrices)
- **Eigenvalues Calculation**: Requires strictly 2x2 matrix input (undefined behavior for other sizes)
```
