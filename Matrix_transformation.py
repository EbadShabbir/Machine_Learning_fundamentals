import numpy as np
from numpy.linalg import LinAlgError

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transforms matrix A using the operation Tâ»Â¹AS where T and S are matrices.
    Returns -1 if the transformation cannot be computed.
    """
    try:
        # Convert to numpy arrays
        A_array = np.array(A, dtype=float)
        T_array = np.array(T, dtype=float)
        S_array = np.array(S, dtype=float)
        
        # Check matrix dimensions compatibility
        if (T_array.shape[0] != T_array.shape[1] or  # T must be square
            T_array.shape[1] != A_array.shape[0] or  # Tâ»Â¹ Ã A compatibility
            A_array.shape[1] != S_array.shape[0]):   # A Ã S compatibility
            return -1
        
        # Check if T is invertible
        T_det = np.linalg.det(T_array)
        if abs(T_det) < 1e-10:  # Essentially zero determinant
            return -1
