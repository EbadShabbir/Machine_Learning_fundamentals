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
- Install numpy 


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





